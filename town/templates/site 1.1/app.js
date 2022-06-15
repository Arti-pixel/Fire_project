let host = "http://127.0.0.1:8000/town";

function submitGeneralData(idForm) {
    let FormElem = document.getElementById(idForm);
    let fd = new FormData(FormElem)

    axios({
            method: 'post',
            url: host + "/api/general-data",
            data: fd,
            headers: { "Content-Type": "multipart/form-data" },
        })
        .then(function(response) {
            cardId = response.data.id;
        });
}

function submitTimeIndicators(idForm) {
    let FormElem = document.getElementById(idForm);
    let fd = new FormData(FormElem)

    fd.append("card_id", cardId)
    axios({
        method: 'post',
        url: host + "/api/general-data",
        data: fd,
        headers: { "Content-Type": "multipart/form-data" },
    })
}

function submitFireDescr(idForm) {
    let FormElem = document.getElementById(idForm);
    let response = fetch(host + "/api/fire-descr", {
        method: "POST",
        mode: "no-cors",
        body: new FormData(FormElem),
    });
}

function submitFireManager(idForm) {
    let FormElem = document.getElementById(idForm);
    let response = fetch(host + "/api/fire-manager", {
        method: "POST",
        mode: "no-cors",
        body: new FormData(FormElem),
    });
}

function submitFireServices(idForm) {
    let FormElem = document.getElementById(idForm);
    let response = fetch(host + "/api/fire-services", {
        method: "POST",
        mode: "no-cors",
        body: new FormData(FormElem),
    });
}

function submitOthFireServices(idForm) {
    let FormElem = document.getElementById(idForm);
    let response = fetch(host + "/api/oth-fire-services", {
        method: "POST",
        mode: "no-cors",
        body: new FormData(FormElem),
    });
}

function submitOthServices(idForm) {
    let FormElem = document.getElementById(idForm);
    let response = fetch(host + "/api/oth-services", {
        method: "POST",
        mode: "no-cors",
        body: new FormData(FormElem),
    });
}

function submitPersonnel(idForm) {
    let FormElem = document.getElementById(idForm);
    let response = fetch(host + "/api/personnel", {
        method: "POST",
        mode: "no-cors",
        body: new FormData(FormElem),
    });
}

function submitFireEquip(idForm) {
    let FormElem = document.getElementById(idForm);
    let response = fetch(host + "/api/fire-equip", {
        method: "POST",
        mode: "no-cors",
        body: new FormData(FormElem),
    });
}

function submitSpecFireEquip(idForm) {
    let FormElem = document.getElementById(idForm);
    let response = fetch(host + "/api/spec-fire-equip", {
        method: "POST",
        mode: "no-cors",
        body: new FormData(FormElem),
    });
}

function submitPrimFireExtingMeans(idForm) {
    let FormElem = document.getElementById(idForm);
    let response = fetch(host + "/api/prim-fire-exting-means", {
        method: "POST",
        mode: "no-cors",
        body: new FormData(FormElem),
    });
}

function submitWaterSupplyOnFire(idForm) {
    let FormElem = document.getElementById(idForm);
    let response = fetch(host + "/api/water-supply-on-fire", {
        method: "POST",
        mode: "no-cors",
        body: new FormData(FormElem),
    });
}

function submitFireExtingAgents(idForm) {
    let FormElem = document.getElementById(idForm);
    let fd = new FormData(FormElem)
    console.log(fd);
    axios({
        method: 'post',
        url: host + "/api/fire-exting-agents",
        data: fd,
        headers: { "Content-Type": "multipart/form-data" },
    })
}

function submitTrunksToExtingFire(idForm) {
    let FormElem = document.getElementById(idForm);
    let response = fetch(host + "/api/trunks-to-exting-fire", {
        method: "POST",
        mode: "no-cors",
        body: new FormData(FormElem),
    });
}

function submitFireConseqPeople(idForm) {
    let FormElem = document.getElementById(idForm);
    let response = fetch(host + "/api/fire-conseq-people", {
        method: "POST",
        mode: "no-cors",
        body: new FormData(FormElem),
    });
}

function submitFireExtingAgentsConsum(idForm) {
    let FormElem = document.getElementById(idForm);
    let response = fetch(host + "/api/fire-exting-agents-consum", {
        method: "POST",
        mode: "no-cors",
        body: new FormData(FormElem),
    });
}

function submitFireConseqBuilding(idForm) {
    let FormElem = document.getElementById(idForm);
    let response = fetch(host + "/api/fire-conseq-building", {
        method: "POST",
        mode: "no-cors",
        body: new FormData(FormElem),
    });
}

function submitFirefightCardAuth(idForm) {
    let FormElem = document.getElementById(idForm);
    let response = fetch(host + "/api/firefight-card-auth", {
        method: "POST",
        mode: "no-cors",
        body: new FormData(FormElem),
    });
}