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
  $(".color-picker").removeClass("border");
  $(this).addClass("border");
});


