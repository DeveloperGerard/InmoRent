from django.contrib import admin
from .models import Propiedad,Comuna
# Register your models here.


class PropiedadInline(admin.TabularInline):
    model =Propiedad
    extra = 1


@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    actions = ["marcar_disponible","marcar_arrendado"]
    list_display = (
         "codigo_propiedad",  
            "direccion"  ,
            "tipo_propiedad",
            "precio_arriendo",  
            "dormitorios",
            "banos",
            "disponible" ,
            "fecha_publicacion", 
            "comuna"
            
         
    )
    search_fields = ["disponible","tipo_propiedad","comuna","codigo_propiedad","direccion"]
    list_filter = ["disponible","tipo_propiedad","comuna"]#clas_comuna
    list_editable = ["disponible","precio_arriendo"]

    #!no me funcion ........ 
    #@admin.display(description="clasificacion columna")
    #def clas_comuna(self,obj):
    #    print(obj.nombre)
    #    return obj.propiedades.clasificacion_columna
    
    #@admin.display(description="nombre comuna")
    #def comuna_nombre(self,obj):
    #    print(obj)
    #     return obj.propiedades.nombre()
   
    @admin.action()
    def marcar_disponible(self,queryset):
        x = queryset.set(disponible = True)

    @admin.action()
    def marcar_arrendado(self,queryset):
        x = queryset.set(disponible = False)
    
@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre", 
            "region", 
            "activa",
            "codigo_clasificacion",
            "total_propiedades_asociadas" 
    )
    @admin.display()
    def total_propiedades_asociadas(self,obj):
        print(obj.nombre)
        print(obj.pro)
        return obj.propiedades.count()



    




    
    