$("#myModal").click(function() {
  $("#exampleModal").modal("toggle");
  $("#exampleModal").modal("hide");
  $("#myModal").css("display", "inline");
});

$(".close").click(function() {
  $(".show").css("display", "none");
  $("#myModal").css("display", "inline");
  $(".modal-backdrop").css("display", "none");
});

$("td").click(function() {
  console.log(
    $(this)
      .children(".date")
      .text()
  );
  console.log($(".month").text());
  string_array = $(".month")
    .text()
    .split(" ");
  console.log(string_array);
  var month = string_array[0];
  var year = string_array[1];
  var day = $(this)
    .children(".date")
    .text();

  $.ajax({
    url: `/calendar/day/` + month + "/" + year + "/" + day,
    method: "get",
    success: function(serverResponse) {
      $(".left-col").html(serverResponse);
    }
  });
});

$(".color-picker").click(function() {
  console.log(
    $(this)
      .children(".color")
      .attr("value")
  );
  var chosen_color = $(this)
    .children(".color")
    .attr("value");
  $("#bg_color").attr("value", chosen_color);
  $("this").removeClass("border");
  $("select option").removeAttr("selected");
  $(this).addClass("border");
  if (chosen_color == "#5549A3") {
    $('select option[value="#5549A3"]').attr("selected", "selected");
  }
  if (chosen_color == "#6d6c6c") {
    $('select option[value="#6d6c6c"]').attr("selected", "selected");
  }
  if (chosen_color == "#2323a0") {
    $('select option[value="#2323a0"]').attr("selected", "selected");
  }
  if (chosen_color == "#940D23") {
    $('select option[value="#940D23"]').attr("selected", "selected");
  }
  if (chosen_color == "#179213") {
    $('select option[value="#179213"]').attr("selected", "selected");
  }
});

$("select").change(function() {
  var select_color = $("select option:selected").attr("value");
  console.log(select_color);
  $(".color-picker").removeClass("border");
  $("#bg_color").attr("value", select_color);
  if (select_color == "#5549A3") {
    $('.color[value="#5549A3"]')
      .parent()
      .addClass("border");
  }
  if (select_color == "#6d6c6c") {
    $('.color[value="#6d6c6c"]')
      .parent()
      .addClass("border");
  }
  if (select_color == "#2323a0") {
    $('.color[value="#2323a0"]')
      .parent()
      .addClass("border");
  }
  if (select_color == "#940D23") {
    $('.color[value="#940D23"]')
      .parent()
      .addClass("border");
  }
  if (select_color == "#179213") {
    $('.color[value="#179213"]')
      .parent()
      .addClass("border");
  }
});

// Drag and Drop
// $( function() {
//   $( "ul, li" ).disableSelection();
//   console.log("dragging")
//   $( ".draggable" ).draggable({
//     helper: "clone",
//     revert:"invalid"
//   })

// } );

// $( "#droppable" ).droppable({
//   drop: function( event, ui ) {
//     $(this).
//   }
// });

//Dark and light mode
const toggleSwitch = document.querySelector(
  '.theme-switch input[type="checkbox"]'
);

function switchTheme(e) {
  if (e.target.checked) {
    document.documentElement.setAttribute("data-theme", "dark");
    localStorage.setItem("theme", "dark"); //add this
  } else {
    document.documentElement.setAttribute("data-theme", "light");
    localStorage.setItem("theme", "light"); //add this
  }
}

toggleSwitch.addEventListener("change", switchTheme, false);

const currentTheme = localStorage.getItem("theme")
  ? localStorage.getItem("theme")
  : null;

if (currentTheme) {
  document.documentElement.setAttribute("data-theme", currentTheme);

  if (currentTheme === "dark") {
    toggleSwitch.checked = true;
  }
}
