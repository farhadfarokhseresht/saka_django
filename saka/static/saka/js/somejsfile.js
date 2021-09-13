
// filter
function filterfun() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("L_filter_id");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

//drup and down list
var AnalytAndDepartment = {};
AnalytAndDepartment[1] = ['FBS','BUN','Cr',"U.A",'TG','CHOL','HDL','LDL','CA' ,'Ph','T.BIL','SGOT','SGPT','ALK','LDH','CPK','AMYL','LIP','CRP','FE','TIBC','ALB','T.PRO','FE','TIBC','ALB','T.Pro','Na','K'];
AnalytAndDepartment[2] = ['Hb','Hct','A1C','INR','PTT'];
AnalytAndDepartment[3] = ['T3','T4','TSH','T3UP','FSH','LH','Prolaction','B.HCG','Ferritin','Vit D','P.S.A','PTH'];

function ChangeAnalytList() {
    var departmentList = document.getElementById("department");
    var modelList = document.getElementById("analytType");
    var selanalyt = departmentList.options[departmentList.selectedIndex].value;
    while (modelList.options.length) {
        modelList.remove(0);
    }
    var analyts = AnalytAndDepartment[selanalyt];
    if (analyts) {
        var i;
        for (i = 0; i < analyts.length; i++) {
            var department = new Option(analyts[i], i);
            modelList.options.add(department);
        }
    }
}

// ??

