$(function () {
    $(".researcher-detail").hide();

    $(".op-edit").click(function () {
        $(".btn-back").show();
        $(".researcher-detail").show();
        $(".researcher-list").hide();
        console.log("op click");
    });

    $(".btn-back").click(function () {
        $(".btn-back").hide();
        $(".researcher-list").show();
        $(".researcher-detail").hide();
        console.log("back click");
    });
});