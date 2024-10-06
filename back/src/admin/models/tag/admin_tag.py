from starlette_admin.contrib.sqla import Admin, ModelView


class AdminTagView(ModelView):
    fields = ["id", "name", "services"]
    exclude_fields = ["services"]
    searchable_fields = ["id", "name"]
    name = "Тэг"
    label = "Тэги"
