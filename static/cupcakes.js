"use strict";

const $cupcakeList = $("#cupcake_list");
const BASE_URL = "http://localhost:5001/api";
const $cupcakeForm = $("#cupcake_form");
const $deleteButton = $(".btn btn-danger");

/** Get list of cupcakes from api */
async function getCupcakes() {
  const response = await axios.get(`${BASE_URL}/cupcakes`);
  return response.data.cupcakes;
}

/** For each cupcake in list call generateHtml */
function displayCupcakes(cupcakes) {
  for (let cupcake of cupcakes) {
    generateHtml(cupcake);
  }
}

/** Generate HTML for cupcake and append to list */
function generateHtml(cupcake) {
  $cupcakeList.append(`
    <div id="c-${cupcake.id}">
        <img src="${cupcake.image}" width="200">
        <li>
            Flavor:${cupcake.flavor} | Size:${cupcake.size} |
            Rating:${cupcake.rating}
        </li>
        <button id="c-${cupcake.id}" class="btn btn-danger">
            X
        </button>
    </div>`);
}

$cupcakeForm.on("submit", handleSubmit);

/**  */
async function handleSubmit(evt) {
  evt.preventDefault();

  const flavor = $("#flavor").val();
  const size = $("#size").val();
  const rating = $("#rating").val();
  const image = $("#image").val();

  const cupcakeResult = await axios.post(`${BASE_URL}/cupcakes`, {
    flavor,
    size,
    rating,
    image,
  });

  generateHtml(cupcakeResult.data.cupcake);
  $cupcakeForm.trigger("reset");
}

$cupcakeList.on("click", ".btn-danger", deleteCupcake);

/** delete cupcake from database and remove from html */
async function deleteCupcake(evt) {
  evt.preventDefault;
  const $cupcake = $(evt.target).closest("div");
  const cupcakeId = $cupcake.attr("id");
  const [_, id] = cupcakeId.split("-");
  const response = await axios.delete(`${BASE_URL}/cupcakes/${id}`);
  console.log(response.data);
  $cupcake.remove();
}

/** Get cupcakes and display */
async function start() {
  const cupcakes = await getCupcakes();
  displayCupcakes(cupcakes);
  console.log("start run");
}
start();
