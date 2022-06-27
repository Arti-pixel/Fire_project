from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, get_user_model, login as user_login
from django.shortcuts import resolve_url
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from .models import GeneralData

from .forms import *


def login(request):

    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    user_login(request, user)
                    return redirect("index")
            else:

                return render(
                    request,
                    "registration/login.html",
                    {"form": form, "fail_login": True},
                )

    else:
        form = AuthenticationForm
    return render(request, "registration/login.html", {"form": form})


def auth(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return redirect("index")
        else:

            return render(
                request, "registration/registration.html", {"user_form": user_form}
            )
    else:
        user_form = UserRegistrationForm()
    return render(request, "registration/registration.html", {"user_form": user_form})


def first_page(request):
    return render(request, "first_page.html")

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  

# defining the function to convert an HTML file to a PDF file
def html_to_pdf(template_src, context_dict={}):
    import weasyprint
    template = get_template(template_src)
    html  = template.render(context_dict)
    
    return HttpResponse(weasyprint.HTML(string=html).write_pdf(), content_type='application/pdf')


def pdf_card_pdf(request, card_id):
    card = get_object_or_404(GeneralData, pk=card_id)
    return html_to_pdf("pdf_card.html", context_dict={"card": card})

def pdf_card(request, card_id):
    card = get_object_or_404(GeneralData, pk=card_id)

    return render(request, "pdf_card.html", context={"card": card})

def index(request):
    params = {}

    settlement = request.GET.get("settlement")
    if settlement:
        params["settlement"] = settlement

    locality_type = request.GET.get("locality_type")
    if locality_type:
        params["locality_type"] = locality_type

    address = request.GET.get("address")
    if address:
        params["address__contains"] = address

    point_of_contact = request.GET.get("point_of_contact")
    if point_of_contact:
        params["point_of_contact"] = point_of_contact

    fire_object = request.GET.get("fire_object")
    if fire_object:
        params["fire_object__contains"] = fire_object

    floors_number = request.GET.get("floors_number")
    if floors_number:
        params["floors_number"] = floors_number

    degree_of_fireres = request.GET.get("degree_of_fireres")
    if degree_of_fireres:
        params["degree_of_fireres"] = degree_of_fireres

    return render(
        request,
        "index.html",
        context={
            "cards": GeneralData.objects.filter(**params),
            "filter_form": GeneralDataFormFilter,
        },
    )


def card_dublicate(request, card_id=None):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    gd.card_id = None
    gd.save()
    new_card_id = gd.card_id

    for rel, model in [
        ("fireconseqbuilding", FireConseqBuilding),
        ("fireconseqpeople", FireConseqPeople),
        ("firedescr", FireDescr),
        ("fireequip", FireEquip),
        ("fireextingagents", FireExtingAgents),
        ("fireextingagentsconsum", FireExtingAgentsConsum),
        ("fireservices", FireServices),
        ("firefightcardauth", FirefightCardAuth),
        ("othfireservices", OthFireServices),
        ("othservices", OthServices),
        ("personnel", Personnel),
        ("primfireextingmeans", PrimFireExtingMeans),
        ("specfireequip", SpecFireEquip),
        ("timeindicators", TimeIndicators),
        ("trunkstoextingfire", TrunksToExtingFire),
        ("watersupplyonfire", WaterSupplyOnFire),
    ]:
        try:
            rel_model = model.objects.get(card_id=card_id)
            kwargs = model_to_dict(rel_model)
            print(kwargs)
            kwargs["card_id"] = gd
            m = model(**kwargs)
            m.save()
            setattr(gd, rel, m)            
        except Exception as e:
            print(e)
        
    return HttpResponseRedirect(resolve_url('index'))


def card_page(request, card_id=None):
    if request.method == "POST":
        if card_id:
            gd = get_object_or_404(GeneralData, card_id=card_id)
        else:
            gd = None

        gd_form = GeneralDataForm(data=request.POST, instance=gd)

        if gd_form.is_valid():
            gd = gd_form.save()
            return HttpResponseRedirect(resolve_url("card-edit", card_id=gd.card_id))
        else:
            return render(
                request,
                "general_data.html",
                context={"card_id": card_id, "gd_form": gd_form},
            )
    else:
        if card_id:
            gd = get_object_or_404(GeneralData, card_id=card_id)
        else:
            gd = None
        gd_form = GeneralDataForm(instance=gd)

    context = {
        "card_id": card_id,
        "gd_form": gd_form,
    }

    return render(request, "general_data.html", context=context)


def fire_manager(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    firemanager = getattr(gd, "firemanager", None)

    if request.method == "POST":
        form = FireManagerForm(
            data=request.POST, initial={"card_id": gd}, instance=firemanager
        )
        if form.is_valid():
            new_firemanager = form.save(commit=False)
            if firemanager is None:
                new_firemanager.card_id = gd

            new_firemanager.save()
            return HttpResponseRedirect(
                resolve_url("fire-manager-edit", card_id=card_id)
            )
        else:
            print(form.errors)
            return render(
                request, "fire_manager.html", context={"form": form, "card_id": card_id}
            )
    else:
        form = FireManagerForm(instance=firemanager)

    return render(
        request, "fire_manager.html", context={"form": form, "card_id": card_id}
    )


def fire_conseq_building(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    fireconseqbuilding = getattr(gd, "fireconseqbuilding", None)

    if request.method == "POST":
        form = FireConseqBuildingForm(
            data=request.POST, initial={"card_id": gd}, instance=fireconseqbuilding
        )
        if form.is_valid():
            new_fireconseqbuilding = form.save(commit=False)
            if fireconseqbuilding is None:
                new_fireconseqbuilding.card_id = gd

            new_fireconseqbuilding.save()
            return HttpResponseRedirect(
                resolve_url("fire-conseq-building", card_id=card_id)
            )
        else:
            return render(
                request,
                "fire_conseq_building.html",
                context={"form": form, "card_id": card_id},
            )
    else:
        form = FireConseqBuildingForm(instance=fireconseqbuilding)

    return render(
        request, "fire_conseq_building.html", context={"form": form, "card_id": card_id}
    )


def fire_conseq_people(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    fireconseqpeople = getattr(gd, "fireconseqpeople", None)

    if request.method == "POST":
        form = FireConseqPeopleForm(
            data=request.POST, initial={"card_id": gd}, instance=fireconseqpeople
        )
        if form.is_valid():
            new_fireconseqpeople = form.save(commit=False)
            if fireconseqpeople is None:
                new_fireconseqpeople.card_id = gd

            new_fireconseqpeople.save()
            return HttpResponseRedirect(
                resolve_url("fire-conseq-people", card_id=card_id)
            )
        else:
            return render(
                request,
                "fire_conseq_people.html",
                context={"form": form, "card_id": card_id},
            )
    else:
        form = FireConseqPeopleForm(instance=fireconseqpeople)

    return render(
        request, "fire_conseq_people.html", context={"form": form, "card_id": card_id}
    )


def fire_descr(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    firedescr = getattr(gd, "firedescr", None)

    if request.method == "POST":
        form = FireDescrForm(
            data=request.POST, initial={"card_id": gd}, instance=firedescr
        )
        if form.is_valid():
            new_firedescr = form.save(commit=False)
            if firedescr is None:
                new_firedescr.card_id = gd

            new_firedescr.save()
            return HttpResponseRedirect(resolve_url("fire-descr", card_id=card_id))
        else:
            return render(
                request, "fire_descr.html", context={"form": form, "card_id": card_id}
            )
    else:
        form = FireDescrForm(instance=firedescr)

    return render(
        request, "fire_descr.html", context={"form": form, "card_id": card_id}
    )


def fire_equip(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    fireequip = getattr(gd, "fireequip", None)

    if request.method == "POST":
        form = FireEquipForm(
            data=request.POST, initial={"card_id": gd}, instance=fireequip
        )
        if form.is_valid():
            new_fireequip = form.save(commit=False)
            if fireequip is None:
                new_fireequip.card_id = gd

            new_fireequip.save()
            return HttpResponseRedirect(resolve_url("fire-equip", card_id=card_id))
        else:
            return render(
                request, "fire_equip.html", context={"form": form, "card_id": card_id}
            )
    else:
        form = FireEquipForm(instance=fireequip)

    return render(
        request, "fire_equip.html", context={"form": form, "card_id": card_id}
    )


def fire_exting_agents(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    fireextingagents = getattr(gd, "fireextingagents", None)

    if request.method == "POST":
        form = FireExtingAgentsForm(
            data=request.POST, initial={"card_id": gd}, instance=fireextingagents
        )
        if form.is_valid():
            new_fireextingagents = form.save(commit=False)
            if fireextingagents is None:
                new_fireextingagents.card_id = gd

            new_fireextingagents.save()
            return HttpResponseRedirect(
                resolve_url("fire-exting-agents", card_id=card_id)
            )
        else:
            return render(
                request,
                "fire_exting_agents.html",
                context={"form": form, "card_id": card_id},
            )
    else:
        form = FireExtingAgentsForm(instance=fireextingagents)

    return render(
        request, "fire_exting_agents.html", context={"form": form, "card_id": card_id}
    )


def fire_exting_agents_consum(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    fireextingagentsconsum = getattr(gd, "fireextingagentsconsum", None)

    if request.method == "POST":
        form = FireExtingAgentsConsumForm(
            data=request.POST, initial={"card_id": gd}, instance=fireextingagentsconsum
        )
        if form.is_valid():
            new_fireextingagentsconsum = form.save(commit=False)
            if fireextingagentsconsum is None:
                new_fireextingagentsconsum.card_id = gd

            new_fireextingagentsconsum.save()
            return HttpResponseRedirect(
                resolve_url("fire-exting-agents-consum", card_id=card_id)
            )
        else:
            return render(
                request,
                "fire_exting_agents_consum.html",
                context={"form": form, "card_id": card_id},
            )
    else:
        form = FireExtingAgentsConsumForm(instance=fireextingagentsconsum)

    return render(
        request,
        "fire_exting_agents_consum.html",
        context={"form": form, "card_id": card_id},
    )


def fire_services(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    fireservices = getattr(gd, "fireservices", None)

    if request.method == "POST":
        form = FireServicesForm(
            data=request.POST, initial={"card_id": gd}, instance=fireservices
        )
        if form.is_valid():
            new_fireservices = form.save(commit=False)
            if fireservices is None:
                new_fireservices.card_id = gd

            new_fireservices.save()
            return HttpResponseRedirect(resolve_url("fire-services", card_id=card_id))
        else:
            return render(
                request,
                "fire_services.html",
                context={"form": form, "card_id": card_id},
            )
    else:
        form = FireServicesForm(instance=fireservices)

    return render(
        request, "fire_services.html", context={"form": form, "card_id": card_id}
    )


def firefight_card_auth(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    firefightcardauth = getattr(gd, "firefightcardauth", None)

    if request.method == "POST":
        form = FirefightCardAuthForm(
            data=request.POST, initial={"card_id": gd}, instance=firefightcardauth
        )
        if form.is_valid():
            new_firefightcardauth = form.save(commit=False)
            if firefightcardauth is None:
                new_firefightcardauth.card_id = gd

            new_firefightcardauth.save()
            return HttpResponseRedirect(
                resolve_url("firefight-card-auth", card_id=card_id)
            )
        else:
            return render(
                request,
                "firefight_card_auth.html",
                context={"form": form, "card_id": card_id},
            )
    else:
        form = FirefightCardAuthForm(instance=firefightcardauth)

    return render(
        request, "firefight_card_auth.html", context={"form": form, "card_id": card_id}
    )


def oth_fire_services(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    othfireservices = getattr(gd, "othfireservices", None)

    if request.method == "POST":
        form = OthFireServicesForm(
            data=request.POST, initial={"card_id": gd}, instance=othfireservices
        )
        if form.is_valid():
            new_othfireservices = form.save(commit=False)
            if othfireservices is None:
                new_othfireservices.card_id = gd

            new_othfireservices.save()
            return HttpResponseRedirect(
                resolve_url("oth-fire-services", card_id=card_id)
            )
        else:
            return render(
                request,
                "oth_fire_services.html",
                context={"form": form, "card_id": card_id},
            )
    else:
        form = OthFireServicesForm(instance=othfireservices)

    return render(
        request, "oth_fire_services.html", context={"form": form, "card_id": card_id}
    )


def oth_services(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    othservices = getattr(gd, "othservices", None)

    if request.method == "POST":
        form = OthServicesForm(
            data=request.POST, initial={"card_id": gd}, instance=othservices
        )
        if form.is_valid():
            new_othservices = form.save(commit=False)
            if othservices is None:
                new_othservices.card_id = gd

            new_othservices.save()
            return HttpResponseRedirect(resolve_url("oth-services", card_id=card_id))
        else:
            return render(
                request, "oth_services.html", context={"form": form, "card_id": card_id}
            )
    else:
        form = OthServicesForm(instance=othservices)

    return render(
        request, "oth_services.html", context={"form": form, "card_id": card_id}
    )


def personnel(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    personnel = getattr(gd, "personnel", None)

    if request.method == "POST":
        form = PersonnelForm(
            data=request.POST, initial={"card_id": gd}, instance=personnel
        )
        if form.is_valid():
            new_personnel = form.save(commit=False)
            if personnel is None:
                new_personnel.card_id = gd

            new_personnel.save()
            return HttpResponseRedirect(resolve_url("personnel", card_id=card_id))
        else:
            return render(
                request, "personnel.html", context={"form": form, "card_id": card_id}
            )
    else:
        form = PersonnelForm(instance=personnel)

    return render(request, "personnel.html", context={"form": form, "card_id": card_id})


def prim_fire_exting_means(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    primfireextingmeans = getattr(gd, "primfireextingmeans", None)

    if request.method == "POST":
        form = PrimFireExtingMeansForm(
            data=request.POST, initial={"card_id": gd}, instance=primfireextingmeans
        )
        if form.is_valid():
            new_primfireextingmeans = form.save(commit=False)
            if primfireextingmeans is None:
                new_primfireextingmeans.card_id = gd

            new_primfireextingmeans.save()
            return HttpResponseRedirect(
                resolve_url("prim-fire-exting-means", card_id=card_id)
            )
        else:
            return render(
                request,
                "prim_fire_exting_means.html",
                context={"form": form, "card_id": card_id},
            )
    else:
        form = PrimFireExtingMeansForm(instance=primfireextingmeans)

    return render(
        request,
        "prim_fire_exting_means.html",
        context={"form": form, "card_id": card_id},
    )


def spec_fire_equip(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    specfireequip = getattr(gd, "specfireequip", None)

    if request.method == "POST":
        form = SpecFireEquipForm(
            data=request.POST, initial={"card_id": gd}, instance=specfireequip
        )
        if form.is_valid():
            new_specfireequip = form.save(commit=False)
            if specfireequip is None:
                new_specfireequip.card_id = gd

            new_specfireequip.save()
            return HttpResponseRedirect(resolve_url("spec-fire-equip", card_id=card_id))
        else:
            return render(
                request,
                "spec_fire_equip.html",
                context={"form": form, "card_id": card_id},
            )
    else:
        form = SpecFireEquipForm(instance=specfireequip)

    return render(
        request, "spec_fire_equip.html", context={"form": form, "card_id": card_id}
    )


def time_indicators(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    timeindicators = getattr(gd, "timeindicators", None)

    if request.method == "POST":
        form = TimeIndicatorsForm(
            data=request.POST, initial={"card_id": gd}, instance=timeindicators
        )
        if form.is_valid():
            new_timeindicators = form.save(commit=False)
            if timeindicators is None:
                new_timeindicators.card_id = gd

            new_timeindicators.save()
            return HttpResponseRedirect(resolve_url("time-indicators", card_id=card_id))
        else:
            return render(
                request,
                "time_indicators.html",
                context={"form": form, "card_id": card_id},
            )
    else:
        form = TimeIndicatorsForm(instance=timeindicators)

    return render(
        request, "time_indicators.html", context={"form": form, "card_id": card_id}
    )


def trunks_to_exting_fire(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    trunkstoextingfire = getattr(gd, "trunkstoextingfire", None)

    if request.method == "POST":
        form = TrunksToExtingFireForm(
            data=request.POST, initial={"card_id": gd}, instance=trunkstoextingfire
        )
        if form.is_valid():
            new_trunkstoextingfire = form.save(commit=False)
            if trunkstoextingfire is None:
                new_trunkstoextingfire.card_id = gd

            new_trunkstoextingfire.save()
            return HttpResponseRedirect(
                resolve_url("trunks-to-exting-fire", card_id=card_id)
            )
        else:
            return render(
                request,
                "trunks_to_exting_fire.html",
                context={"form": form, "card_id": card_id},
            )
    else:
        form = TrunksToExtingFireForm(instance=trunkstoextingfire)

    return render(
        request,
        "trunks_to_exting_fire.html",
        context={"form": form, "card_id": card_id},
    )


def water_supply_on_fire(request, card_id):
    gd = get_object_or_404(GeneralData, card_id=card_id)
    watersupplyonfire = getattr(gd, "watersupplyonfire", None)

    if request.method == "POST":
        form = WaterSupplyOnFireForm(
            data=request.POST, initial={"card_id": gd}, instance=watersupplyonfire
        )
        if form.is_valid():
            new_watersupplyonfire = form.save(commit=False)
            if watersupplyonfire is None:
                new_watersupplyonfire.card_id = gd

            new_watersupplyonfire.save()
            return HttpResponseRedirect(
                resolve_url("water-supply-on-fire", card_id=card_id)
            )
        else:
            return render(
                request,
                "water_supply_on_fire.html",
                context={"form": form, "card_id": card_id},
            )
    else:
        form = WaterSupplyOnFireForm(instance=watersupplyonfire)

    return render(
        request, "water_supply_on_fire.html", context={"form": form, "card_id": card_id}
    )
