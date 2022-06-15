const fireData = [{
    "settlement": "Мурманск",
    "locality_type": "город",
    "address":"Кирова 42, 42",
    "point_of_contact":"1 ПСЧ",
    "fire_object":"1.1. какое-то здание",
    "floors_number":"2",
    "degree_of_fireres":"|",
    "id": "1",
  },
  {
    "settlement": "Кировск",
    "locality_type": "посёлок",
    "address":"Пушкина 41, 50",
    "point_of_contact":"2 ПСЧ",
    "fire_object":"2.3. какое-то другое здание",
    "floors_number":"5",
    "degree_of_fireres":"||",
    "id": "2",
  },
  {
    "settlement": "Апатиты",
    "locality_type": "другой населённый",
    "address":"Ленина 82, 15",
    "point_of_contact":"3 ПСЧ",
    "fire_object":"2.28. вообще не здание",
    "floors_number":"",
    "degree_of_fireres":"|||",
    "id": "3",
  },
]

function fireTemplate(fireCase){
  return `<tr>
    <td>${fireCase.settlement}</td>
    <td>${fireCase.locality_type}</td>
    <td>${fireCase.address}</td>
    <td>${fireCase.point_of_contact}</td>
    <td>${fireCase.fire_object}</td>
    <td>${fireCase.floors_number}</td>
    <td>${fireCase.degree_of_fireres}</td>
    <td><a class="btn btn-primary butn-color" href="forms.html?id=${fireCase.id}">Редактировать запись</a></td>
    </tr>`;
};

mytablebody = document.createElement("tbody");

mytablebody.innerHTML = `
${fireData.map(fireTemplate).join("")}
`;

document.getElementById("app").appendChild(mytablebody);