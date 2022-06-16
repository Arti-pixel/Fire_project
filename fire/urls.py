#gathered_static_path = os.path.join(settings.BASE_DIR, settings.STATIC_ROOT)
from . import views
from django.urls import path


urlpatterns = [    
    path('',views.index, name='index'),
    path('first_page.html',views.first_page),
    path('card', views.card_page, name="card-create"),
    path('card/<int:card_id>/', views.card_page, name="card-edit"),
    path('card/<int:card_id>/fire-manager', views.fire_manager, name="fire-manager"),
    path('card/<int:card_id>/fire-conseq-building', views.fire_conseq_building, name="fire-conseq-building"),
    path('card/<int:card_id>/fire-conseq-people', views.fire_conseq_people, name="fire-conseq-people"),
    path('card/<int:card_id>/fire-descr', views.fire_descr, name="fire-descr"),
    path('card/<int:card_id>/fire-equip', views.fire_equip, name="fire-equip"),
    path('card/<int:card_id>/fire-exting-agents', views.fire_exting_agents, name="fire-exting-agents"),
    path('card/<int:card_id>/fire-exting-agents-consum', views.fire_exting_agents_consum, name="fire-exting-agents-consum"),
    path('card/<int:card_id>/fire-services', views.fire_services, name="fire-services"),
    path('card/<int:card_id>/firefight-card-auth', views.firefight_card_auth, name="firefight-card-auth"),
    path('card/<int:card_id>/oth-fire-services', views.oth_fire_services, name="oth-fire-services"),
    path('card/<int:card_id>/oth-services', views.oth_services, name="oth-services"),
    path('card/<int:card_id>/personnel', views.personnel, name="personnel"),
    path('card/<int:card_id>/prim-fire-exting-means', views.prim_fire_exting_means, name="prim-fire-exting-means"),
    path('card/<int:card_id>/spec-fire-equip', views.spec_fire_equip, name="spec-fire-equip"),
    path('card/<int:card_id>/time-indicators', views.time_indicators, name="time-indicators"),
    path('card/<int:card_id>/trunks-to-exting-fire', views.trunks_to_exting_fire, name="trunks-to-exting-fire"),
    path('card/<int:card_id>/water-supply-on-fire', views.water_supply_on_fire, name="water-supply-on-fire"),
]
