google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawChart);

function drawChart() {
    $.get("../res/data/kzn1993.csv", function(csvString) {
	var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
	var data = new google.visualization.arrayToDataTable(arrayData);
	var view = new google.visualization.DataView(data);
	view.setColumns([0,1]);

	var options = {
	    title: "KwaZulu-Natal Household Survey (1993)",
	    hAxis: {title: data.getColumnLabel(0), minValue: data.getColumnRange(0).min, maxValue: data.getColumnRange(0).max},
	    vAxis: {title: data.getColumnLabel(1), minValue: data.getColumnRange(1).min, maxValue: data.getColumnRange(1).max},
	    legend: 'none'
	};

	var chart = new google.visualization.ScatterChart(document.getElementById('chart'));
	chart.draw(view, options);

	for (var i=0; i<arrayData[0].length; i++){
	    $("select").append("<option value='" + i + "'>" + arrayData[0][i] + "</option");
	}

	$("#domain option[value='0']").attr("selected","selected");
	$("#range option[value='1']").attr("selected","selected");

	$("select").click(function(){
	    var domain = +$("#domain option:selected").val();
	    var range = +$("#range option:selected").val();

	    view.setColumns([domain,range]);
	    options.hAxis.title = data.getColumnLabel(domain);
	    options.hAxis.minValue = data.getColumnRange(domain).min;
	    options.hAxis.maxValue = data.getColumnRange(domain).max;
	    options.vAxis.title = data.getColumnLabel(range);
	    options.vAxis.minValue = data.getColumnRange(range).min;
	    options.vAxis.maxValue = data.getColumnRange(range).max;

	    chart.draw(view, options);
	});
	
    });
}
