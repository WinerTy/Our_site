from sqlalchemy.future import select
from fastapi import APIRouter, Depends, HTTPException

from src.config.database.db_helper import db_helper


from sqlalchemy.ext.asyncio import AsyncSession
from src.database.db import get_session
from ...schemas.brief_schema import *
from src.models.brief_model import Brief, Service
from ...repositories.brief_repo import (
    ServiceRepository,
    BriefRepository,
    service_repository,
    brief_repository,
)


router = APIRouter(prefix="/service", tags=["service"])


@router.post("/", response_model=ServiceResponce)
async def create_service(
    service_data: ServiceCreate, session: AsyncSession = Depends(get_session)
) -> ServiceResponce:
    data = service_data.dict()
    service = await service_repository.create(data)
    return service


# NOT WORKED :)
@router.post("/briefs/")
async def create_brief(data: BriefCreate, session: AsyncSession = Depends(get_session)):

    brief = await brief_repository.create(data.dict(exclude="services"))

    for service_data in data.services:
        service = await service_repository.get_single(id=service_data.id)
        if not service:
            raise HTTPException(
                status_code=404, detail=f"Service with id {service_data.id} not found"
            )
        brief.services.append(service)

    await brief_repository.update(brief.id, services=brief.services)

    return {"id": brief.id, "client_name": brief.client_name}


# WORKER EXAMPLE
# @router.post("/briefs/")
# async def create_brief(
#     brief_data: BriefCreate, session: AsyncSession = Depends(get_session)
# ):
#     brief = Brief(
#         company_did=brief_data.company_did,
#         concompetitors=brief_data.concompetitors,
#         additional_comment=brief_data.additional_comment,
#         client_name=brief_data.client_name,
#         client_phone=brief_data.client_phone,
#         client_email=brief_data.client_email,
#         client_task=brief_data.client_task,
#         client_company=brief_data.client_company,
#         client_site=brief_data.client_site,
#     )

#     for service_data in brief_data.services:
#         service = await session.get(Service, service_data.id)
#         if not service:
#             raise HTTPException(
#                 status_code=404, detail=f"Service with id {service_data.id} not found"
#             )
#         brief.services.append(service)

#     session.add(brief)
#     await session.commit()
#     await session.refresh(brief)

#     return {"id": brief.id, "client_name": brief.client_name}
