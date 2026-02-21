from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from networks.models import NetworkNode


@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "city",
        "supplier_link",
        "name_product",
        "model",
        "debt",
        "created_at",
        "level",
    )
    list_filter = ("city",)
    actions = [clear_debt]

    def supplier_link(self, obj):
        if obj.supplier:
            url = reverse("admin:networks_networknode_change", args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return "Нет поставщика"

    supplier_link.short_description = "Поставщик"
