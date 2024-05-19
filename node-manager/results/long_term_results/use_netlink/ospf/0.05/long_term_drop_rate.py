import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


data1 = [
  {
    "real-time": "1715791720.081422",
    "sim-time": "11.464",
    "now drop rate": "13.179%",
    "now drop cnt": "13.206"
  },
  {
    "real-time": "1715791721.091543",
    "sim-time": "12.474",
    "now drop rate": "7.558%",
    "now drop cnt": "15.207"
  },
  {
    "real-time": "1715791722.095707",
    "sim-time": "13.478",
    "now drop rate": "5.511%",
    "now drop cnt": "16.623"
  },
  {
    "real-time": "1715791723.099361",
    "sim-time": "14.481",
    "now drop rate": "4.466%",
    "now drop cnt": "17.952"
  },
  {
    "real-time": "1715791724.101204",
    "sim-time": "15.483",
    "now drop rate": "3.817%",
    "now drop cnt": "19.165"
  },
  {
    "real-time": "1715791725.104406",
    "sim-time": "16.487",
    "now drop rate": "3.404%",
    "now drop cnt": "20.510"
  },
  {
    "real-time": "1715791726.107359",
    "sim-time": "17.490",
    "now drop rate": "3.102%",
    "now drop cnt": "21.802"
  },
  {
    "real-time": "1715791727.112461",
    "sim-time": "18.495",
    "now drop rate": "2.902%",
    "now drop cnt": "23.311"
  },
  {
    "real-time": "1715791728.117325",
    "sim-time": "19.499",
    "now drop rate": "2.742%",
    "now drop cnt": "24.784"
  },
  {
    "real-time": "1715791729.123674",
    "sim-time": "20.506",
    "now drop rate": "2.632%",
    "now drop cnt": "26.434"
  },
  {
    "real-time": "1715791730.128119",
    "sim-time": "21.510",
    "now drop rate": "2.523%",
    "now drop cnt": "27.875"
  },
  {
    "real-time": "1715791731.135899",
    "sim-time": "22.518",
    "now drop rate": "2.461%",
    "now drop cnt": "29.673"
  },
  {
    "real-time": "1715791732.143323",
    "sim-time": "23.525",
    "now drop rate": "2.785%",
    "now drop cnt": "36.385"
  },
  {
    "real-time": "1715791733.143987",
    "sim-time": "24.526",
    "now drop rate": "2.590%",
    "now drop cnt": "36.429"
  },
  {
    "real-time": "1715791734.147031",
    "sim-time": "25.529",
    "now drop rate": "2.506%",
    "now drop cnt": "37.760"
  },
  {
    "real-time": "1715791735.192220",
    "sim-time": "26.585",
    "now drop rate": "3.926%",
    "now drop cnt": "63.294"
  },
  {
    "real-time": "1715791736.203894",
    "sim-time": "27.586",
    "now drop rate": "3.239%",
    "now drop cnt": "55.459"
  },
  {
    "real-time": "1715791737.213418",
    "sim-time": "28.596",
    "now drop rate": "3.332%",
    "now drop cnt": "60.414"
  },
  {
    "real-time": "1715791738.220781",
    "sim-time": "29.607",
    "now drop rate": "3.321%",
    "now drop cnt": "63.574"
  },
  {
    "real-time": "1715791739.233170",
    "sim-time": "30.615",
    "now drop rate": "3.046%",
    "now drop cnt": "61.383"
  },
  {
    "real-time": "1715791740.237272",
    "sim-time": "31.619",
    "now drop rate": "2.967%",
    "now drop cnt": "62.782"
  },
  {
    "real-time": "1715791741.241466",
    "sim-time": "32.624",
    "now drop rate": "2.898%",
    "now drop cnt": "64.215"
  },
  {
    "real-time": "1715791742.247810",
    "sim-time": "33.630",
    "now drop rate": "2.842%",
    "now drop cnt": "65.840"
  },
  {
    "real-time": "1715791743.317433",
    "sim-time": "34.710",
    "now drop rate": "6.178%",
    "now drop cnt": "149.817"
  },
  {
    "real-time": "1715791744.336845",
    "sim-time": "35.719",
    "now drop rate": "5.651%",
    "now drop cnt": "142.742"
  },
  {
    "real-time": "1715791745.339252",
    "sim-time": "36.721",
    "now drop rate": "5.483%",
    "now drop cnt": "143.985"
  },
  {
    "real-time": "1715791746.343771",
    "sim-time": "37.726",
    "now drop rate": "5.335%",
    "now drop cnt": "145.461"
  },
  {
    "real-time": "1715791747.347331",
    "sim-time": "38.730",
    "now drop rate": "5.193%",
    "now drop cnt": "146.795"
  },
  {
    "real-time": "1715791748.773069",
    "sim-time": "40.165",
    "now drop rate": "7.217%",
    "now drop cnt": "214.379"
  },
  {
    "real-time": "1715791749.790233",
    "sim-time": "41.172",
    "now drop rate": "6.483%",
    "now drop cnt": "199.084"
  },
  {
    "real-time": "1715791750.794101",
    "sim-time": "42.176",
    "now drop rate": "6.321%",
    "now drop cnt": "200.478"
  },
  {
    "real-time": "1715791751.797649",
    "sim-time": "43.180",
    "now drop rate": "6.168%",
    "now drop cnt": "201.811"
  },
  {
    "real-time": "1715791752.800283",
    "sim-time": "44.182",
    "now drop rate": "6.022%",
    "now drop cnt": "203.070"
  },
  {
    "real-time": "1715791753.802990",
    "sim-time": "45.185",
    "now drop rate": "5.885%",
    "now drop cnt": "204.363"
  },
  {
    "real-time": "1715791754.803694",
    "sim-time": "46.186",
    "now drop rate": "5.750%",
    "now drop cnt": "205.432"
  },
  {
    "real-time": "1715791755.809546",
    "sim-time": "47.192",
    "now drop rate": "5.636%",
    "now drop cnt": "207.027"
  },
  {
    "real-time": "1715791756.813010",
    "sim-time": "48.195",
    "now drop rate": "5.522%",
    "now drop cnt": "208.372"
  },
  {
    "real-time": "1715791758.239397",
    "sim-time": "49.622",
    "now drop rate": "7.534%",
    "now drop cnt": "295.026"
  },
  {
    "real-time": "1715791759.232032",
    "sim-time": "50.623",
    "now drop rate": "7.350%",
    "now drop cnt": "295.182"
  },
  {
    "real-time": "1715791760.244610",
    "sim-time": "51.627",
    "now drop rate": "7.155%",
    "now drop cnt": "294.519"
  },
  {
    "real-time": "1715791761.252173",
    "sim-time": "52.634",
    "now drop rate": "7.025%",
    "now drop cnt": "296.284"
  },
  {
    "real-time": "1715791762.257392",
    "sim-time": "53.640",
    "now drop rate": "6.875%",
    "now drop cnt": "296.854"
  },
  {
    "real-time": "1715791763.260365",
    "sim-time": "54.643",
    "now drop rate": "6.747%",
    "now drop cnt": "298.103"
  },
  {
    "real-time": "1715791764.263662",
    "sim-time": "55.646",
    "now drop rate": "6.627%",
    "now drop cnt": "299.423"
  },
  {
    "real-time": "1715791765.268407",
    "sim-time": "56.651",
    "now drop rate": "6.493%",
    "now drop cnt": "299.917"
  },
  {
    "real-time": "1715791766.273493",
    "sim-time": "57.656",
    "now drop rate": "6.387%",
    "now drop cnt": "301.406"
  },
  {
    "real-time": "1715791767.276861",
    "sim-time": "58.659",
    "now drop rate": "6.281%",
    "now drop cnt": "302.728"
  },
  {
    "real-time": "1715791768.279343",
    "sim-time": "59.662",
    "now drop rate": "6.362%",
    "now drop cnt": "312.995"
  },
  {
    "real-time": "1715791769.287381",
    "sim-time": "60.669",
    "now drop rate": "6.248%",
    "now drop cnt": "313.713"
  },
  {
    "real-time": "1715791770.290356",
    "sim-time": "61.673",
    "now drop rate": "6.153%",
    "now drop cnt": "315.105"
  },
  {
    "real-time": "1715791771.747020",
    "sim-time": "63.129",
    "now drop rate": "6.964%",
    "now drop cnt": "366.770"
  },
  {
    "real-time": "1715791772.750284",
    "sim-time": "64.132",
    "now drop rate": "6.858%",
    "now drop cnt": "368.093"
  },
  {
    "real-time": "1715791773.753128",
    "sim-time": "65.136",
    "now drop rate": "6.756%",
    "now drop cnt": "369.393"
  },
  {
    "real-time": "1715791774.756283",
    "sim-time": "66.138",
    "now drop rate": "6.658%",
    "now drop cnt": "370.679"
  },
  {
    "real-time": "1715791775.759631",
    "sim-time": "67.142",
    "now drop rate": "6.563%",
    "now drop cnt": "372.017"
  },
  {
    "real-time": "1715791776.763285",
    "sim-time": "68.145",
    "now drop rate": "6.473%",
    "now drop cnt": "373.381"
  },
  {
    "real-time": "1715791777.938015",
    "sim-time": "69.150",
    "now drop rate": "6.386%",
    "now drop cnt": "374.802"
  },
  {
    "real-time": "1715791779.025517",
    "sim-time": "70.408",
    "now drop rate": "7.217%",
    "now drop cnt": "432.632"
  },
  {
    "real-time": "1715791780.057655",
    "sim-time": "71.440",
    "now drop rate": "8.132%",
    "now drop cnt": "495.851"
  },
  {
    "real-time": "1715791781.062081",
    "sim-time": "72.444",
    "now drop rate": "8.023%",
    "now drop cnt": "497.275"
  },
  {
    "real-time": "1715791782.065627",
    "sim-time": "73.448",
    "now drop rate": "7.901%",
    "now drop cnt": "497.632"
  },
  {
    "real-time": "1715791783.066128",
    "sim-time": "74.448",
    "now drop rate": "9.231%",
    "now drop cnt": "590.667"
  },
  {
    "real-time": "1715791784.071561",
    "sim-time": "75.454",
    "now drop rate": "9.112%",
    "now drop cnt": "592.215"
  },
  {
    "real-time": "1715791785.076120",
    "sim-time": "76.459",
    "now drop rate": "8.996%",
    "now drop cnt": "593.700"
  },
  {
    "real-time": "1715791786.083444",
    "sim-time": "77.466",
    "now drop rate": "8.826%",
    "now drop cnt": "591.409"
  },
  {
    "real-time": "1715791787.089182",
    "sim-time": "78.471",
    "now drop rate": "8.704%",
    "now drop cnt": "591.973"
  },
  {
    "real-time": "1715791788.968904",
    "sim-time": "80.273",
    "now drop rate": "9.943%",
    "now drop cnt": "694.129"
  },
  {
    "real-time": "1715791789.894070",
    "sim-time": "81.276",
    "now drop rate": "9.906%",
    "now drop cnt": "701.462"
  },
  {
    "real-time": "1715791790.898463",
    "sim-time": "82.281",
    "now drop rate": "9.787%",
    "now drop cnt": "702.912"
  },
  {
    "real-time": "1715791791.903793",
    "sim-time": "83.285",
    "now drop rate": "9.672%",
    "now drop cnt": "704.345"
  },
  {
    "real-time": "1715791792.906359",
    "sim-time": "84.288",
    "now drop rate": "9.559%",
    "now drop cnt": "705.689"
  },
  {
    "real-time": "1715791793.910744",
    "sim-time": "85.293",
    "now drop rate": "9.450%",
    "now drop cnt": "707.133"
  },
  {
    "real-time": "1715791794.914763",
    "sim-time": "86.297",
    "now drop rate": "9.343%",
    "now drop cnt": "708.538"
  },
  {
    "real-time": "1715791795.917295",
    "sim-time": "87.300",
    "now drop rate": "9.238%",
    "now drop cnt": "709.797"
  },
  {
    "real-time": "1715791796.920538",
    "sim-time": "88.303",
    "now drop rate": "9.123%",
    "now drop cnt": "710.112"
  },
  {
    "real-time": "1715791797.923174",
    "sim-time": "89.305",
    "now drop rate": "9.023%",
    "now drop cnt": "711.384"
  },
  {
    "real-time": "1715791798.926613",
    "sim-time": "90.309",
    "now drop rate": "8.926%",
    "now drop cnt": "712.714"
  },
  {
    "real-time": "1715791799.929206",
    "sim-time": "91.311",
    "now drop rate": "8.831%",
    "now drop cnt": "713.983"
  },
  {
    "real-time": "1715791800.930902",
    "sim-time": "92.313",
    "now drop rate": "8.749%",
    "now drop cnt": "716.154"
  },
  {
    "real-time": "1715791801.932575",
    "sim-time": "93.315",
    "now drop rate": "8.658%",
    "now drop cnt": "717.314"
  },
  {
    "real-time": "1715791802.939491",
    "sim-time": "94.321",
    "now drop rate": "8.573%",
    "now drop cnt": "718.904"
  },
  {
    "real-time": "1715791803.947907",
    "sim-time": "95.330",
    "now drop rate": "8.494%",
    "now drop cnt": "720.852"
  },
  {
    "real-time": "1715791804.951539",
    "sim-time": "96.334",
    "now drop rate": "8.411%",
    "now drop cnt": "722.231"
  },
  {
    "real-time": "1715791805.961766",
    "sim-time": "97.344",
    "now drop rate": "8.336%",
    "now drop cnt": "724.232"
  },
  {
    "real-time": "1715791806.965474",
    "sim-time": "98.348",
    "now drop rate": "8.256%",
    "now drop cnt": "725.610"
  },
  {
    "real-time": "1715791807.970235",
    "sim-time": "99.352",
    "now drop rate": "8.179%",
    "now drop cnt": "727.045"
  },
  {
    "real-time": "1715791808.977562",
    "sim-time": "100.360",
    "now drop rate": "8.107%",
    "now drop cnt": "728.818"
  },
  {
    "real-time": "1715791809.987474",
    "sim-time": "101.370",
    "now drop rate": "8.039%",
    "now drop cnt": "730.812"
  },
  {
    "real-time": "1715791810.997173",
    "sim-time": "102.379",
    "now drop rate": "7.972%",
    "now drop cnt": "732.777"
  },
  {
    "real-time": "1715791812.000353",
    "sim-time": "103.382",
    "now drop rate": "7.900%",
    "now drop cnt": "734.068"
  },
  {
    "real-time": "1715791813.006171",
    "sim-time": "104.388",
    "now drop rate": "7.832%",
    "now drop cnt": "735.669"
  },
  {
    "real-time": "1715791814.009556",
    "sim-time": "105.392",
    "now drop rate": "7.764%",
    "now drop cnt": "737.025"
  },
  {
    "real-time": "1715791815.012337",
    "sim-time": "106.395",
    "now drop rate": "7.696%",
    "now drop cnt": "738.295"
  },
  {
    "real-time": "1715791816.015107",
    "sim-time": "107.397",
    "now drop rate": "7.630%",
    "now drop cnt": "739.574"
  },
  {
    "real-time": "1715791817.021284",
    "sim-time": "108.404",
    "now drop rate": "7.568%",
    "now drop cnt": "741.200"
  },
  {
    "real-time": "1715791818.023075",
    "sim-time": "109.405",
    "now drop rate": "7.503%",
    "now drop cnt": "742.372"
  },
  {
    "real-time": "1715791819.029958",
    "sim-time": "110.413",
    "now drop rate": "7.445%",
    "now drop cnt": "744.114"
  },
  {
    "drop rate": " 7.320%",
    "delay": " 162.229"
  }
]
data2 = [
  {
    "real-time": "1715792057.196723",
    "sim-time": "11.371",
    "now drop rate": "13.086%",
    "now drop cnt": "13.098"
  },
  {
    "real-time": "1715792058.200040",
    "sim-time": "12.374",
    "now drop rate": "7.201%",
    "now drop cnt": "14.433"
  },
  {
    "real-time": "1715792059.205641",
    "sim-time": "13.380",
    "now drop rate": "5.316%",
    "now drop cnt": "16.000"
  },
  {
    "real-time": "1715792060.211000",
    "sim-time": "14.385",
    "now drop rate": "4.363%",
    "now drop cnt": "17.519"
  },
  {
    "real-time": "1715792061.215474",
    "sim-time": "15.390",
    "now drop rate": "3.780%",
    "now drop cnt": "18.976"
  },
  {
    "real-time": "1715792062.219350",
    "sim-time": "16.393",
    "now drop rate": "3.380%",
    "now drop cnt": "20.360"
  },
  {
    "real-time": "1715792063.223787",
    "sim-time": "17.398",
    "now drop rate": "3.102%",
    "now drop cnt": "21.802"
  },
  {
    "real-time": "1715792064.227026",
    "sim-time": "18.401",
    "now drop rate": "2.880%",
    "now drop cnt": "23.127"
  },
  {
    "real-time": "1715792065.230621",
    "sim-time": "19.405",
    "now drop rate": "2.710%",
    "now drop cnt": "24.487"
  },
  {
    "real-time": "1715792066.238034",
    "sim-time": "20.412",
    "now drop rate": "2.612%",
    "now drop cnt": "26.230"
  },
  {
    "real-time": "1715792067.244857",
    "sim-time": "21.419",
    "now drop rate": "2.524%",
    "now drop cnt": "27.883"
  },
  {
    "real-time": "1715792068.248713",
    "sim-time": "22.423",
    "now drop rate": "2.431%",
    "now drop cnt": "29.304"
  },
  {
    "real-time": "1715792069.254331",
    "sim-time": "23.428",
    "now drop rate": "2.822%",
    "now drop cnt": "36.852"
  },
  {
    "real-time": "1715792070.259220",
    "sim-time": "24.433",
    "now drop rate": "2.726%",
    "now drop cnt": "38.331"
  },
  {
    "real-time": "1715792071.265838",
    "sim-time": "25.439",
    "now drop rate": "2.651%",
    "now drop cnt": "39.942"
  },
  {
    "real-time": "1715792072.270698",
    "sim-time": "26.445",
    "now drop rate": "2.580%",
    "now drop cnt": "41.472"
  },
  {
    "real-time": "1715792073.273378",
    "sim-time": "27.448",
    "now drop rate": "2.739%",
    "now drop cnt": "46.780"
  },
  {
    "real-time": "1715792074.277383",
    "sim-time": "28.451",
    "now drop rate": "2.663%",
    "now drop cnt": "48.143"
  },
  {
    "real-time": "1715792075.273424",
    "sim-time": "29.456",
    "now drop rate": "2.598%",
    "now drop cnt": "49.593"
  },
  {
    "real-time": "1715792076.285666",
    "sim-time": "30.460",
    "now drop rate": "2.438%",
    "now drop cnt": "48.986"
  },
  {
    "real-time": "1715792077.290011",
    "sim-time": "31.463",
    "now drop rate": "2.385%",
    "now drop cnt": "50.297"
  },
  {
    "real-time": "1715792078.291871",
    "sim-time": "32.466",
    "now drop rate": "2.336%",
    "now drop cnt": "51.608"
  },
  {
    "real-time": "1715792079.297250",
    "sim-time": "33.471",
    "now drop rate": "2.301%",
    "now drop cnt": "53.152"
  },
  {
    "real-time": "1715792080.650900",
    "sim-time": "34.835",
    "now drop rate": "6.153%",
    "now drop cnt": "150.523"
  },
  {
    "real-time": "1715792081.664741",
    "sim-time": "35.839",
    "now drop rate": "5.689%",
    "now drop cnt": "144.903"
  },
  {
    "real-time": "1715792082.666219",
    "sim-time": "36.840",
    "now drop rate": "5.517%",
    "now drop cnt": "146.038"
  },
  {
    "real-time": "1715792083.668070",
    "sim-time": "37.842",
    "now drop rate": "5.360%",
    "now drop cnt": "147.245"
  },
  {
    "real-time": "1715792084.671230",
    "sim-time": "38.845",
    "now drop rate": "5.217%",
    "now drop cnt": "148.551"
  },
  {
    "real-time": "1715792085.675979",
    "sim-time": "39.850",
    "now drop rate": "5.327%",
    "now drop cnt": "157.049"
  },
  {
    "real-time": "1715792086.681714",
    "sim-time": "40.856",
    "now drop rate": "5.202%",
    "now drop cnt": "158.597"
  },
  {
    "real-time": "1715792087.688093",
    "sim-time": "41.862",
    "now drop rate": "4.898%",
    "now drop cnt": "154.236"
  },
  {
    "real-time": "1715792088.693618",
    "sim-time": "42.866",
    "now drop rate": "4.787%",
    "now drop cnt": "155.568"
  },
  {
    "real-time": "1715792089.693978",
    "sim-time": "43.868",
    "now drop rate": "4.681%",
    "now drop cnt": "156.807"
  },
  {
    "real-time": "1715792090.698689",
    "sim-time": "44.873",
    "now drop rate": "4.588%",
    "now drop cnt": "158.290"
  },
  {
    "real-time": "1715792091.703536",
    "sim-time": "45.878",
    "now drop rate": "4.501%",
    "now drop cnt": "159.805"
  },
  {
    "real-time": "1715792092.710252",
    "sim-time": "46.883",
    "now drop rate": "4.418%",
    "now drop cnt": "161.310"
  },
  {
    "real-time": "1715792093.712999",
    "sim-time": "47.887",
    "now drop rate": "4.337%",
    "now drop cnt": "162.725"
  },
  {
    "real-time": "1715792094.705560",
    "sim-time": "48.889",
    "now drop rate": "4.384%",
    "now drop cnt": "168.878"
  },
  {
    "real-time": "1715792095.718907",
    "sim-time": "49.893",
    "now drop rate": "4.284%",
    "now drop cnt": "169.321"
  },
  {
    "real-time": "1715792096.722827",
    "sim-time": "50.897",
    "now drop rate": "4.212%",
    "now drop cnt": "170.704"
  },
  {
    "real-time": "1715792097.728374",
    "sim-time": "51.903",
    "now drop rate": "4.148%",
    "now drop cnt": "172.268"
  },
  {
    "real-time": "1715792098.736039",
    "sim-time": "52.910",
    "now drop rate": "4.067%",
    "now drop cnt": "173.012"
  },
  {
    "real-time": "1715792099.742836",
    "sim-time": "53.917",
    "now drop rate": "4.012%",
    "now drop cnt": "174.713"
  },
  {
    "real-time": "1715792100.748430",
    "sim-time": "54.923",
    "now drop rate": "3.956%",
    "now drop cnt": "176.263"
  },
  {
    "real-time": "1715792101.755323",
    "sim-time": "55.929",
    "now drop rate": "3.884%",
    "now drop cnt": "176.951"
  },
  {
    "real-time": "1715792102.757629",
    "sim-time": "56.932",
    "now drop rate": "3.827%",
    "now drop cnt": "178.184"
  },
  {
    "real-time": "1715792103.761526",
    "sim-time": "57.936",
    "now drop rate": "3.775%",
    "now drop cnt": "179.572"
  },
  {
    "real-time": "1715792104.766415",
    "sim-time": "58.941",
    "now drop rate": "3.728%",
    "now drop cnt": "181.063"
  },
  {
    "real-time": "1715792105.769209",
    "sim-time": "59.943",
    "now drop rate": "3.759%",
    "now drop cnt": "186.353"
  },
  {
    "real-time": "1715792106.772545",
    "sim-time": "60.947",
    "now drop rate": "3.711%",
    "now drop cnt": "187.672"
  },
  {
    "real-time": "1715792107.777355",
    "sim-time": "61.951",
    "now drop rate": "3.667%",
    "now drop cnt": "189.158"
  },
  {
    "real-time": "1715792108.921916",
    "sim-time": "63.097",
    "now drop rate": "4.489%",
    "now drop cnt": "236.669"
  },
  {
    "real-time": "1715792109.927600",
    "sim-time": "64.102",
    "now drop rate": "4.433%",
    "now drop cnt": "238.180"
  },
  {
    "real-time": "1715792110.930965",
    "sim-time": "65.105",
    "now drop rate": "4.376%",
    "now drop cnt": "239.530"
  },
  {
    "real-time": "1715792111.933445",
    "sim-time": "66.108",
    "now drop rate": "4.320%",
    "now drop cnt": "240.764"
  },
  {
    "real-time": "1715792112.940085",
    "sim-time": "67.114",
    "now drop rate": "4.273%",
    "now drop cnt": "242.441"
  },
  {
    "real-time": "1715792113.943890",
    "sim-time": "68.118",
    "now drop rate": "4.222%",
    "now drop cnt": "243.816"
  },
  {
    "real-time": "1715792115.114200",
    "sim-time": "69.298",
    "now drop rate": "4.783%",
    "now drop cnt": "281.853"
  },
  {
    "real-time": "1715792116.128094",
    "sim-time": "70.302",
    "now drop rate": "4.075%",
    "now drop cnt": "244.206"
  },
  {
    "real-time": "1715792117.186323",
    "sim-time": "71.361",
    "now drop rate": "4.920%",
    "now drop cnt": "300.071"
  },
  {
    "real-time": "1715792118.194275",
    "sim-time": "72.368",
    "now drop rate": "4.869%",
    "now drop cnt": "301.850"
  },
  {
    "real-time": "1715792119.197458",
    "sim-time": "73.372",
    "now drop rate": "4.812%",
    "now drop cnt": "303.171"
  },
  {
    "real-time": "1715792120.199282",
    "sim-time": "74.373",
    "now drop rate": "4.990%",
    "now drop cnt": "319.346"
  },
  {
    "real-time": "1715792121.203209",
    "sim-time": "75.377",
    "now drop rate": "4.934%",
    "now drop cnt": "320.740"
  },
  {
    "real-time": "1715792122.209417",
    "sim-time": "76.384",
    "now drop rate": "4.883%",
    "now drop cnt": "322.365"
  },
  {
    "real-time": "1715792123.200208",
    "sim-time": "77.384",
    "now drop rate": "4.886%",
    "now drop cnt": "327.423"
  },
  {
    "real-time": "1715792124.219341",
    "sim-time": "78.393",
    "now drop rate": "4.709%",
    "now drop cnt": "320.354"
  },
  {
    "real-time": "1715792125.498858",
    "sim-time": "79.673",
    "now drop rate": "5.214%",
    "now drop cnt": "361.337"
  },
  {
    "real-time": "1715792126.504359",
    "sim-time": "80.678",
    "now drop rate": "5.161%",
    "now drop cnt": "362.861"
  },
  {
    "real-time": "1715792127.509377",
    "sim-time": "81.684",
    "now drop rate": "5.109%",
    "now drop cnt": "364.365"
  },
  {
    "real-time": "1715792128.512702",
    "sim-time": "82.687",
    "now drop rate": "5.057%",
    "now drop cnt": "365.701"
  },
  {
    "real-time": "1715792129.517520",
    "sim-time": "83.692",
    "now drop rate": "5.008%",
    "now drop cnt": "367.175"
  },
  {
    "real-time": "1715792130.524148",
    "sim-time": "84.698",
    "now drop rate": "4.962%",
    "now drop cnt": "368.833"
  },
  {
    "real-time": "1715792131.528478",
    "sim-time": "85.703",
    "now drop rate": "4.915%",
    "now drop cnt": "370.276"
  },
  {
    "real-time": "1715792132.533952",
    "sim-time": "86.708",
    "now drop rate": "4.857%",
    "now drop cnt": "370.804"
  },
  {
    "real-time": "1715792133.540568",
    "sim-time": "87.715",
    "now drop rate": "4.816%",
    "now drop cnt": "372.475"
  },
  {
    "real-time": "1715792134.545684",
    "sim-time": "88.720",
    "now drop rate": "4.774%",
    "now drop cnt": "374.031"
  },
  {
    "real-time": "1715792135.549291",
    "sim-time": "89.723",
    "now drop rate": "4.730%",
    "now drop cnt": "375.352"
  },
  {
    "real-time": "1715792136.552721",
    "sim-time": "90.727",
    "now drop rate": "4.688%",
    "now drop cnt": "376.702"
  },
  {
    "real-time": "1715792137.555754",
    "sim-time": "91.731",
    "now drop rate": "4.648%",
    "now drop cnt": "378.137"
  },
  {
    "real-time": "1715792138.561025",
    "sim-time": "92.735",
    "now drop rate": "4.607%",
    "now drop cnt": "379.486"
  },
  {
    "real-time": "1715792139.568392",
    "sim-time": "93.743",
    "now drop rate": "4.573%",
    "now drop cnt": "381.273"
  },
  {
    "real-time": "1715792140.570909",
    "sim-time": "94.745",
    "now drop rate": "4.533%",
    "now drop cnt": "382.514"
  },
  {
    "real-time": "1715792141.572268",
    "sim-time": "95.747",
    "now drop rate": "4.494%",
    "now drop cnt": "383.665"
  },
  {
    "real-time": "1715792142.573962",
    "sim-time": "96.748",
    "now drop rate": "4.455%",
    "now drop cnt": "384.823"
  },
  {
    "real-time": "1715792143.576207",
    "sim-time": "97.750",
    "now drop rate": "4.418%",
    "now drop cnt": "386.047"
  },
  {
    "real-time": "1715792144.580831",
    "sim-time": "98.755",
    "now drop rate": "4.407%",
    "now drop cnt": "389.494"
  },
  {
    "real-time": "1715792145.586439",
    "sim-time": "99.761",
    "now drop rate": "4.375%",
    "now drop cnt": "391.067"
  },
  {
    "real-time": "1715792146.590329",
    "sim-time": "100.764",
    "now drop rate": "4.342%",
    "now drop cnt": "392.456"
  },
  {
    "real-time": "1715792147.597339",
    "sim-time": "101.771",
    "now drop rate": "4.312%",
    "now drop cnt": "394.156"
  },
  {
    "real-time": "1715792148.601290",
    "sim-time": "102.776",
    "now drop rate": "4.281%",
    "now drop cnt": "395.634"
  },
  {
    "real-time": "1715792149.606437",
    "sim-time": "103.781",
    "now drop rate": "4.251%",
    "now drop cnt": "397.123"
  },
  {
    "real-time": "1715792150.611357",
    "sim-time": "104.785",
    "now drop rate": "4.221%",
    "now drop cnt": "398.541"
  },
  {
    "real-time": "1715792151.615200",
    "sim-time": "105.790",
    "now drop rate": "4.192%",
    "now drop cnt": "399.966"
  },
  {
    "real-time": "1715792152.619245",
    "sim-time": "106.793",
    "now drop rate": "4.162%",
    "now drop cnt": "401.356"
  },
  {
    "real-time": "1715792153.620950",
    "sim-time": "107.795",
    "now drop rate": "4.132%",
    "now drop cnt": "402.519"
  },
  {
    "real-time": "1715792154.625835",
    "sim-time": "108.800",
    "now drop rate": "4.104%",
    "now drop cnt": "404.001"
  },
  {
    "real-time": "1715792155.631624",
    "sim-time": "109.806",
    "now drop rate": "4.079%",
    "now drop cnt": "405.585"
  },
  {
    "drop rate": " 3.940%",
    "delay": " 161.942"
  }
]
data3 = [
  {
    "real-time": "1715792397.345404",
    "sim-time": "11.598",
    "now drop rate": "14.817%",
    "now drop cnt": "14.959"
  },
  {
    "real-time": "1715792398.349427",
    "sim-time": "12.602",
    "now drop rate": "8.113%",
    "now drop cnt": "16.333"
  },
  {
    "real-time": "1715792399.352041",
    "sim-time": "13.604",
    "now drop rate": "5.840%",
    "now drop cnt": "17.613"
  },
  {
    "real-time": "1715792400.358590",
    "sim-time": "14.611",
    "now drop rate": "4.788%",
    "now drop cnt": "19.261"
  },
  {
    "real-time": "1715792401.361897",
    "sim-time": "15.614",
    "now drop rate": "4.097%",
    "now drop cnt": "20.591"
  },
  {
    "real-time": "1715792402.364795",
    "sim-time": "16.617",
    "now drop rate": "3.630%",
    "now drop cnt": "21.884"
  },
  {
    "real-time": "1715792403.370269",
    "sim-time": "17.623",
    "now drop rate": "3.331%",
    "now drop cnt": "23.434"
  },
  {
    "real-time": "1715792404.373445",
    "sim-time": "18.626",
    "now drop rate": "3.080%",
    "now drop cnt": "24.752"
  },
  {
    "real-time": "1715792405.380981",
    "sim-time": "19.633",
    "now drop rate": "2.930%",
    "now drop cnt": "26.501"
  },
  {
    "real-time": "1715792406.384449",
    "sim-time": "20.637",
    "now drop rate": "2.772%",
    "now drop cnt": "27.859"
  },
  {
    "real-time": "1715792407.389413",
    "sim-time": "21.642",
    "now drop rate": "2.655%",
    "now drop cnt": "29.349"
  },
  {
    "real-time": "1715792408.391060",
    "sim-time": "22.644",
    "now drop rate": "2.532%",
    "now drop cnt": "30.520"
  },
  {
    "real-time": "1715792409.395427",
    "sim-time": "23.648",
    "now drop rate": "2.752%",
    "now drop cnt": "35.945"
  },
  {
    "real-time": "1715792410.400966",
    "sim-time": "24.653",
    "now drop rate": "2.666%",
    "now drop cnt": "37.502"
  },
  {
    "real-time": "1715792411.407923",
    "sim-time": "25.660",
    "now drop rate": "2.601%",
    "now drop cnt": "39.207"
  },
  {
    "real-time": "1715792412.413230",
    "sim-time": "26.666",
    "now drop rate": "2.784%",
    "now drop cnt": "44.755"
  },
  {
    "real-time": "1715792413.417341",
    "sim-time": "27.670",
    "now drop rate": "2.702%",
    "now drop cnt": "46.147"
  },
  {
    "real-time": "1715792414.421555",
    "sim-time": "28.674",
    "now drop rate": "2.630%",
    "now drop cnt": "47.563"
  },
  {
    "real-time": "1715792415.428423",
    "sim-time": "29.681",
    "now drop rate": "2.474%",
    "now drop cnt": "47.242"
  },
  {
    "real-time": "1715792416.432661",
    "sim-time": "30.685",
    "now drop rate": "2.422%",
    "now drop cnt": "48.670"
  },
  {
    "real-time": "1715792417.438270",
    "sim-time": "31.691",
    "now drop rate": "2.380%",
    "now drop cnt": "50.217"
  },
  {
    "real-time": "1715792418.442809",
    "sim-time": "32.695",
    "now drop rate": "2.338%",
    "now drop cnt": "51.688"
  },
  {
    "real-time": "1715792419.447771",
    "sim-time": "33.700",
    "now drop rate": "2.301%",
    "now drop cnt": "53.184"
  },
  {
    "real-time": "1715792420.453475",
    "sim-time": "34.706",
    "now drop rate": "3.016%",
    "now drop cnt": "72.747"
  },
  {
    "real-time": "1715792421.460574",
    "sim-time": "35.713",
    "now drop rate": "2.884%",
    "now drop cnt": "72.456"
  },
  {
    "real-time": "1715792422.465204",
    "sim-time": "36.718",
    "now drop rate": "2.830%",
    "now drop cnt": "73.936"
  },
  {
    "real-time": "1715792423.469849",
    "sim-time": "37.722",
    "now drop rate": "2.778%",
    "now drop cnt": "75.382"
  },
  {
    "real-time": "1715792424.474065",
    "sim-time": "38.726",
    "now drop rate": "2.730%",
    "now drop cnt": "76.814"
  },
  {
    "real-time": "1715792425.484583",
    "sim-time": "39.737",
    "now drop rate": "3.665%",
    "now drop cnt": "106.822"
  },
  {
    "real-time": "1715792426.490075",
    "sim-time": "40.742",
    "now drop rate": "3.428%",
    "now drop cnt": "103.370"
  },
  {
    "real-time": "1715792427.493318",
    "sim-time": "41.746",
    "now drop rate": "3.362%",
    "now drop cnt": "104.737"
  },
  {
    "real-time": "1715792428.498942",
    "sim-time": "42.751",
    "now drop rate": "3.305%",
    "now drop cnt": "106.299"
  },
  {
    "real-time": "1715792429.504282",
    "sim-time": "43.757",
    "now drop rate": "3.251%",
    "now drop cnt": "107.838"
  },
  {
    "real-time": "1715792430.508466",
    "sim-time": "44.761",
    "now drop rate": "3.196%",
    "now drop cnt": "109.231"
  },
  {
    "real-time": "1715792431.512905",
    "sim-time": "45.765",
    "now drop rate": "3.147%",
    "now drop cnt": "110.696"
  },
  {
    "real-time": "1715792432.515893",
    "sim-time": "46.769",
    "now drop rate": "3.428%",
    "now drop cnt": "124.025"
  },
  {
    "real-time": "1715792433.522875",
    "sim-time": "47.775",
    "now drop rate": "3.380%",
    "now drop cnt": "125.694"
  },
  {
    "real-time": "1715792435.150836",
    "sim-time": "49.403",
    "now drop rate": "4.960%",
    "now drop cnt": "192.507"
  },
  {
    "real-time": "1715792436.154408",
    "sim-time": "50.407",
    "now drop rate": "4.868%",
    "now drop cnt": "193.845"
  },
  {
    "real-time": "1715792437.155859",
    "sim-time": "51.408",
    "now drop rate": "4.777%",
    "now drop cnt": "194.977"
  },
  {
    "real-time": "1715792438.161565",
    "sim-time": "52.414",
    "now drop rate": "4.700%",
    "now drop cnt": "196.572"
  },
  {
    "real-time": "1715792439.168858",
    "sim-time": "53.421",
    "now drop rate": "4.606%",
    "now drop cnt": "197.283"
  },
  {
    "real-time": "1715792440.174588",
    "sim-time": "54.427",
    "now drop rate": "4.582%",
    "now drop cnt": "200.852"
  },
  {
    "real-time": "1715792441.178440",
    "sim-time": "55.431",
    "now drop rate": "4.488%",
    "now drop cnt": "201.241"
  },
  {
    "real-time": "1715792442.182414",
    "sim-time": "56.435",
    "now drop rate": "4.420%",
    "now drop cnt": "202.638"
  },
  {
    "real-time": "1715792443.185261",
    "sim-time": "57.438",
    "now drop rate": "4.353%",
    "now drop cnt": "203.926"
  },
  {
    "real-time": "1715792444.190115",
    "sim-time": "58.442",
    "now drop rate": "4.292%",
    "now drop cnt": "205.379"
  },
  {
    "real-time": "1715792445.195735",
    "sim-time": "59.448",
    "now drop rate": "4.236%",
    "now drop cnt": "206.988"
  },
  {
    "real-time": "1715792446.197608",
    "sim-time": "60.451",
    "now drop rate": "4.256%",
    "now drop cnt": "212.221"
  },
  {
    "real-time": "1715792447.206409",
    "sim-time": "61.458",
    "now drop rate": "4.206%",
    "now drop cnt": "213.964"
  },
  {
    "real-time": "1715792448.212008",
    "sim-time": "62.464",
    "now drop rate": "4.156%",
    "now drop cnt": "215.612"
  },
  {
    "real-time": "1715792449.215001",
    "sim-time": "63.467",
    "now drop rate": "4.820%",
    "now drop cnt": "254.896"
  },
  {
    "real-time": "1715792450.221376",
    "sim-time": "64.474",
    "now drop rate": "4.761%",
    "now drop cnt": "256.548"
  },
  {
    "real-time": "1715792451.224733",
    "sim-time": "65.477",
    "now drop rate": "4.698%",
    "now drop cnt": "257.883"
  },
  {
    "real-time": "1715792452.232125",
    "sim-time": "66.485",
    "now drop rate": "4.645%",
    "now drop cnt": "259.628"
  },
  {
    "real-time": "1715792453.237807",
    "sim-time": "67.489",
    "now drop rate": "4.589%",
    "now drop cnt": "261.105"
  },
  {
    "real-time": "1715792454.241993",
    "sim-time": "68.494",
    "now drop rate": "4.535%",
    "now drop cnt": "262.600"
  },
  {
    "real-time": "1715792455.249944",
    "sim-time": "69.502",
    "now drop rate": "4.437%",
    "now drop cnt": "261.413"
  },
  {
    "real-time": "1715792456.254136",
    "sim-time": "70.507",
    "now drop rate": "4.386%",
    "now drop cnt": "262.818"
  },
  {
    "real-time": "1715792457.262345",
    "sim-time": "71.515",
    "now drop rate": "4.442%",
    "now drop cnt": "270.642"
  },
  {
    "real-time": "1715792458.266747",
    "sim-time": "72.519",
    "now drop rate": "4.393%",
    "now drop cnt": "272.067"
  },
  {
    "real-time": "1715792459.307958",
    "sim-time": "73.560",
    "now drop rate": "4.402%",
    "now drop cnt": "277.199"
  },
  {
    "real-time": "1715792460.310851",
    "sim-time": "74.563",
    "now drop rate": "4.353%",
    "now drop cnt": "278.491"
  },
  {
    "real-time": "1715792461.316481",
    "sim-time": "75.569",
    "now drop rate": "4.309%",
    "now drop cnt": "280.026"
  },
  {
    "real-time": "1715792462.320486",
    "sim-time": "76.573",
    "now drop rate": "4.265%",
    "now drop cnt": "281.443"
  },
  {
    "real-time": "1715792463.322687",
    "sim-time": "77.575",
    "now drop rate": "4.145%",
    "now drop cnt": "277.661"
  },
  {
    "real-time": "1715792464.325423",
    "sim-time": "78.578",
    "now drop rate": "4.103%",
    "now drop cnt": "278.976"
  },
  {
    "real-time": "1715792465.335775",
    "sim-time": "79.588",
    "now drop rate": "4.406%",
    "now drop cnt": "303.985"
  },
  {
    "real-time": "1715792466.342064",
    "sim-time": "80.594",
    "now drop rate": "4.351%",
    "now drop cnt": "304.593"
  },
  {
    "real-time": "1715792467.346153",
    "sim-time": "81.599",
    "now drop rate": "4.310%",
    "now drop cnt": "306.075"
  },
  {
    "real-time": "1715792468.349264",
    "sim-time": "82.602",
    "now drop rate": "4.268%",
    "now drop cnt": "307.330"
  },
  {
    "real-time": "1715792469.352499",
    "sim-time": "83.605",
    "now drop rate": "4.227%",
    "now drop cnt": "308.656"
  },
  {
    "real-time": "1715792470.356073",
    "sim-time": "84.608",
    "now drop rate": "4.188%",
    "now drop cnt": "310.003"
  },
  {
    "real-time": "1715792471.360181",
    "sim-time": "85.613",
    "now drop rate": "4.151%",
    "now drop cnt": "311.426"
  },
  {
    "real-time": "1715792472.362308",
    "sim-time": "86.615",
    "now drop rate": "4.125%",
    "now drop cnt": "313.630"
  },
  {
    "real-time": "1715792473.371395",
    "sim-time": "87.624",
    "now drop rate": "4.070%",
    "now drop cnt": "313.540"
  },
  {
    "real-time": "1715792474.374470",
    "sim-time": "88.627",
    "now drop rate": "4.034%",
    "now drop cnt": "314.846"
  },
  {
    "real-time": "1715792475.382941",
    "sim-time": "89.635",
    "now drop rate": "4.006%",
    "now drop cnt": "316.693"
  },
  {
    "real-time": "1715792476.390252",
    "sim-time": "90.643",
    "now drop rate": "3.978%",
    "now drop cnt": "318.430"
  },
  {
    "real-time": "1715792477.394081",
    "sim-time": "91.646",
    "now drop rate": "3.945%",
    "now drop cnt": "319.813"
  },
  {
    "real-time": "1715792478.398176",
    "sim-time": "92.650",
    "now drop rate": "3.914%",
    "now drop cnt": "321.214"
  },
  {
    "real-time": "1715792479.402597",
    "sim-time": "93.655",
    "now drop rate": "3.884%",
    "now drop cnt": "322.662"
  },
  {
    "real-time": "1715792480.406432",
    "sim-time": "94.659",
    "now drop rate": "3.854%",
    "now drop cnt": "324.042"
  },
  {
    "real-time": "1715792481.408965",
    "sim-time": "95.661",
    "now drop rate": "3.824%",
    "now drop cnt": "325.304"
  },
  {
    "real-time": "1715792482.412192",
    "sim-time": "96.665",
    "now drop rate": "3.795%",
    "now drop cnt": "326.622"
  },
  {
    "real-time": "1715792483.414943",
    "sim-time": "97.667",
    "now drop rate": "3.765%",
    "now drop cnt": "327.887"
  },
  {
    "real-time": "1715792484.418286",
    "sim-time": "98.671",
    "now drop rate": "3.738%",
    "now drop cnt": "329.232"
  },
  {
    "real-time": "1715792485.425478",
    "sim-time": "99.678",
    "now drop rate": "3.737%",
    "now drop cnt": "332.960"
  },
  {
    "real-time": "1715792486.429284",
    "sim-time": "100.682",
    "now drop rate": "3.711%",
    "now drop cnt": "334.324"
  },
  {
    "real-time": "1715792487.433613",
    "sim-time": "101.686",
    "now drop rate": "3.685%",
    "now drop cnt": "335.739"
  },
  {
    "real-time": "1715792488.438430",
    "sim-time": "102.691",
    "now drop rate": "3.684%",
    "now drop cnt": "339.311"
  },
  {
    "real-time": "1715792489.446722",
    "sim-time": "103.699",
    "now drop rate": "3.652%",
    "now drop cnt": "340.082"
  },
  {
    "real-time": "1715792490.451764",
    "sim-time": "104.704",
    "now drop rate": "3.629%",
    "now drop cnt": "341.584"
  },
  {
    "real-time": "1715792491.455062",
    "sim-time": "105.707",
    "now drop rate": "3.605%",
    "now drop cnt": "342.907"
  },
  {
    "real-time": "1715792492.459372",
    "sim-time": "106.712",
    "now drop rate": "3.582%",
    "now drop cnt": "344.328"
  },
  {
    "real-time": "1715792493.462210",
    "sim-time": "107.714",
    "now drop rate": "3.558%",
    "now drop cnt": "345.595"
  },
  {
    "real-time": "1715792494.465003",
    "sim-time": "108.717",
    "now drop rate": "3.535%",
    "now drop cnt": "346.914"
  },
  {
    "real-time": "1715792495.469434",
    "sim-time": "109.722",
    "now drop rate": "3.514%",
    "now drop cnt": "348.348"
  },
  {
    "real-time": "1715792496.472988",
    "sim-time": "110.725",
    "now drop rate": "3.492%",
    "now drop cnt": "349.701"
  },
  {
    "drop rate": " 3.360%",
    "delay": " 161.276"
  }
]
data4 = [
  {
    "real-time": "1715792735.001336",
    "sim-time": "11.478",
    "now drop rate": "14.096%",
    "now drop cnt": "14.112"
  },
  {
    "real-time": "1715792736.004316",
    "sim-time": "12.481",
    "now drop rate": "7.696%",
    "now drop cnt": "15.424"
  },
  {
    "real-time": "1715792737.008416",
    "sim-time": "13.485",
    "now drop rate": "5.589%",
    "now drop cnt": "16.812"
  },
  {
    "real-time": "1715792738.010490",
    "sim-time": "14.487",
    "now drop rate": "4.491%",
    "now drop cnt": "18.008"
  },
  {
    "real-time": "1715792739.012748",
    "sim-time": "15.489",
    "now drop rate": "3.838%",
    "now drop cnt": "19.239"
  },
  {
    "real-time": "1715792740.017693",
    "sim-time": "16.494",
    "now drop rate": "3.446%",
    "now drop cnt": "20.733"
  },
  {
    "real-time": "1715792741.020714",
    "sim-time": "17.497",
    "now drop rate": "3.138%",
    "now drop cnt": "22.033"
  },
  {
    "real-time": "1715792742.023899",
    "sim-time": "18.500",
    "now drop rate": "2.911%",
    "now drop cnt": "23.356"
  },
  {
    "real-time": "1715792743.026566",
    "sim-time": "19.503",
    "now drop rate": "2.727%",
    "now drop cnt": "24.617"
  },
  {
    "real-time": "1715792744.033680",
    "sim-time": "20.510",
    "now drop rate": "2.624%",
    "now drop cnt": "26.331"
  },
  {
    "real-time": "1715792745.038045",
    "sim-time": "21.516",
    "now drop rate": "2.528%",
    "now drop cnt": "27.912"
  },
  {
    "real-time": "1715792746.041156",
    "sim-time": "22.517",
    "now drop rate": "2.415%",
    "now drop cnt": "29.077"
  },
  {
    "real-time": "1715792747.043961",
    "sim-time": "23.520",
    "now drop rate": "2.864%",
    "now drop cnt": "37.363"
  },
  {
    "real-time": "1715792748.047313",
    "sim-time": "24.523",
    "now drop rate": "2.755%",
    "now drop cnt": "38.694"
  },
  {
    "real-time": "1715792749.051011",
    "sim-time": "25.527",
    "now drop rate": "2.662%",
    "now drop cnt": "40.059"
  },
  {
    "real-time": "1715792750.054786",
    "sim-time": "26.531",
    "now drop rate": "3.140%",
    "now drop cnt": "50.417"
  },
  {
    "real-time": "1715792751.060425",
    "sim-time": "27.537",
    "now drop rate": "2.991%",
    "now drop cnt": "51.029"
  },
  {
    "real-time": "1715792752.064618",
    "sim-time": "28.541",
    "now drop rate": "2.903%",
    "now drop cnt": "52.439"
  },
  {
    "real-time": "1715792753.072879",
    "sim-time": "29.549",
    "now drop rate": "2.897%",
    "now drop cnt": "55.245"
  },
  {
    "real-time": "1715792754.081291",
    "sim-time": "30.558",
    "now drop rate": "2.644%",
    "now drop cnt": "53.095"
  },
  {
    "real-time": "1715792755.086517",
    "sim-time": "31.563",
    "now drop rate": "2.591%",
    "now drop cnt": "54.624"
  },
  {
    "real-time": "1715792756.091533",
    "sim-time": "32.568",
    "now drop rate": "2.540%",
    "now drop cnt": "56.118"
  },
  {
    "real-time": "1715792757.098122",
    "sim-time": "33.574",
    "now drop rate": "2.501%",
    "now drop cnt": "57.757"
  },
  {
    "real-time": "1715792758.107653",
    "sim-time": "34.584",
    "now drop rate": "2.768%",
    "now drop cnt": "66.728"
  },
  {
    "real-time": "1715792759.110332",
    "sim-time": "35.587",
    "now drop rate": "2.668%",
    "now drop cnt": "67.003"
  },
  {
    "real-time": "1715792760.113030",
    "sim-time": "36.589",
    "now drop rate": "2.614%",
    "now drop cnt": "68.263"
  },
  {
    "real-time": "1715792761.116166",
    "sim-time": "37.592",
    "now drop rate": "2.566%",
    "now drop cnt": "69.584"
  },
  {
    "real-time": "1715792762.117933",
    "sim-time": "38.594",
    "now drop rate": "2.516%",
    "now drop cnt": "70.754"
  },
  {
    "real-time": "1715792763.566621",
    "sim-time": "40.043",
    "now drop rate": "4.757%",
    "now drop cnt": "140.633"
  },
  {
    "real-time": "1715792764.570631",
    "sim-time": "41.047",
    "now drop rate": "4.516%",
    "now drop cnt": "138.042"
  },
  {
    "real-time": "1715792765.572966",
    "sim-time": "42.049",
    "now drop rate": "4.411%",
    "now drop cnt": "139.265"
  },
  {
    "real-time": "1715792766.574548",
    "sim-time": "43.051",
    "now drop rate": "4.312%",
    "now drop cnt": "140.449"
  },
  {
    "real-time": "1715792767.577262",
    "sim-time": "44.053",
    "now drop rate": "4.220%",
    "now drop cnt": "141.679"
  },
  {
    "real-time": "1715792768.580420",
    "sim-time": "45.057",
    "now drop rate": "4.136%",
    "now drop cnt": "143.016"
  },
  {
    "real-time": "1715792769.582185",
    "sim-time": "46.058",
    "now drop rate": "4.051%",
    "now drop cnt": "144.130"
  },
  {
    "real-time": "1715792770.585516",
    "sim-time": "47.063",
    "now drop rate": "3.980%",
    "now drop cnt": "145.620"
  },
  {
    "real-time": "1715792771.588277",
    "sim-time": "48.065",
    "now drop rate": "3.905%",
    "now drop cnt": "146.799"
  },
  {
    "real-time": "1715792772.996796",
    "sim-time": "49.473",
    "now drop rate": "5.633%",
    "now drop cnt": "219.680"
  },
  {
    "real-time": "1715792774.003190",
    "sim-time": "50.479",
    "now drop rate": "5.532%",
    "now drop cnt": "221.282"
  },
  {
    "real-time": "1715792775.005658",
    "sim-time": "51.482",
    "now drop rate": "5.427%",
    "now drop cnt": "222.541"
  },
  {
    "real-time": "1715792776.012361",
    "sim-time": "52.489",
    "now drop rate": "5.336%",
    "now drop cnt": "224.196"
  },
  {
    "real-time": "1715792777.017560",
    "sim-time": "53.494",
    "now drop rate": "5.224%",
    "now drop cnt": "224.730"
  },
  {
    "real-time": "1715792778.022126",
    "sim-time": "54.498",
    "now drop rate": "5.138%",
    "now drop cnt": "226.172"
  },
  {
    "real-time": "1715792779.026338",
    "sim-time": "55.502",
    "now drop rate": "5.032%",
    "now drop cnt": "226.590"
  },
  {
    "real-time": "1715792780.030991",
    "sim-time": "56.507",
    "now drop rate": "4.955%",
    "now drop cnt": "228.067"
  },
  {
    "real-time": "1715792781.032939",
    "sim-time": "57.509",
    "now drop rate": "4.875%",
    "now drop cnt": "229.267"
  },
  {
    "real-time": "1715792782.035102",
    "sim-time": "58.511",
    "now drop rate": "4.798%",
    "now drop cnt": "230.485"
  },
  {
    "real-time": "1715792783.038076",
    "sim-time": "59.514",
    "now drop rate": "4.726%",
    "now drop cnt": "231.774"
  },
  {
    "real-time": "1715792784.042246",
    "sim-time": "60.518",
    "now drop rate": "4.740%",
    "now drop cnt": "237.184"
  },
  {
    "real-time": "1715792785.050515",
    "sim-time": "61.527",
    "now drop rate": "4.682%",
    "now drop cnt": "239.018"
  },
  {
    "real-time": "1715792786.053538",
    "sim-time": "62.530",
    "now drop rate": "4.617%",
    "now drop cnt": "240.324"
  },
  {
    "real-time": "1715792787.054770",
    "sim-time": "63.531",
    "now drop rate": "5.286%",
    "now drop cnt": "280.448"
  },
  {
    "real-time": "1715792788.058667",
    "sim-time": "64.535",
    "now drop rate": "5.214%",
    "now drop cnt": "281.850"
  },
  {
    "real-time": "1715792789.060976",
    "sim-time": "65.537",
    "now drop rate": "5.141%",
    "now drop cnt": "283.066"
  },
  {
    "real-time": "1715792790.065190",
    "sim-time": "66.542",
    "now drop rate": "5.075%",
    "now drop cnt": "284.502"
  },
  {
    "real-time": "1715792791.068985",
    "sim-time": "67.545",
    "now drop rate": "5.009%",
    "now drop cnt": "285.863"
  },
  {
    "real-time": "1715792792.073059",
    "sim-time": "68.549",
    "now drop rate": "4.946%",
    "now drop cnt": "287.255"
  },
  {
    "real-time": "1715792793.080299",
    "sim-time": "69.557",
    "now drop rate": "4.841%",
    "now drop cnt": "285.996"
  },
  {
    "real-time": "1715792794.084449",
    "sim-time": "70.561",
    "now drop rate": "4.784%",
    "now drop cnt": "287.418"
  },
  {
    "real-time": "1715792795.093225",
    "sim-time": "71.569",
    "now drop rate": "4.833%",
    "now drop cnt": "295.292"
  },
  {
    "real-time": "1715792796.097205",
    "sim-time": "72.573",
    "now drop rate": "4.778%",
    "now drop cnt": "296.688"
  },
  {
    "real-time": "1715792797.980176",
    "sim-time": "74.456",
    "now drop rate": "6.127%",
    "now drop cnt": "391.994"
  },
  {
    "real-time": "1715792798.984246",
    "sim-time": "75.460",
    "now drop rate": "6.054%",
    "now drop cnt": "393.383"
  },
  {
    "real-time": "1715792799.993412",
    "sim-time": "76.470",
    "now drop rate": "5.990%",
    "now drop cnt": "395.310"
  },
  {
    "real-time": "1715792800.995944",
    "sim-time": "77.472",
    "now drop rate": "5.845%",
    "now drop cnt": "391.576"
  },
  {
    "real-time": "1715792802.001379",
    "sim-time": "78.477",
    "now drop rate": "5.780%",
    "now drop cnt": "393.055"
  },
  {
    "real-time": "1715792803.063493",
    "sim-time": "79.540",
    "now drop rate": "6.086%",
    "now drop cnt": "420.328"
  },
  {
    "real-time": "1715792804.071170",
    "sim-time": "80.547",
    "now drop rate": "6.009%",
    "now drop cnt": "421.069"
  },
  {
    "real-time": "1715792805.077212",
    "sim-time": "81.554",
    "now drop rate": "5.947%",
    "now drop cnt": "422.702"
  },
  {
    "real-time": "1715792806.082680",
    "sim-time": "82.559",
    "now drop rate": "5.885%",
    "now drop cnt": "424.235"
  },
  {
    "real-time": "1715792807.087476",
    "sim-time": "83.564",
    "now drop rate": "5.825%",
    "now drop cnt": "425.712"
  },
  {
    "real-time": "1715792808.091853",
    "sim-time": "84.568",
    "now drop rate": "5.765%",
    "now drop cnt": "427.162"
  },
  {
    "real-time": "1715792809.095896",
    "sim-time": "85.572",
    "now drop rate": "5.707%",
    "now drop cnt": "428.546"
  },
  {
    "real-time": "1715792810.096753",
    "sim-time": "86.574",
    "now drop rate": "5.660%",
    "now drop cnt": "430.703"
  },
  {
    "real-time": "1715792811.103484",
    "sim-time": "87.580",
    "now drop rate": "5.581%",
    "now drop cnt": "430.320"
  },
  {
    "real-time": "1715792812.105994",
    "sim-time": "88.582",
    "now drop rate": "5.525%",
    "now drop cnt": "431.547"
  },
  {
    "real-time": "1715792813.108259",
    "sim-time": "89.584",
    "now drop rate": "5.471%",
    "now drop cnt": "432.793"
  },
  {
    "real-time": "1715792814.110272",
    "sim-time": "90.586",
    "now drop rate": "5.417%",
    "now drop cnt": "433.994"
  },
  {
    "real-time": "1715792815.112131",
    "sim-time": "91.588",
    "now drop rate": "5.365%",
    "now drop cnt": "435.180"
  },
  {
    "real-time": "1715792816.115795",
    "sim-time": "92.592",
    "now drop rate": "5.316%",
    "now drop cnt": "436.543"
  },
  {
    "real-time": "1715792817.118575",
    "sim-time": "93.595",
    "now drop rate": "5.267%",
    "now drop cnt": "437.815"
  },
  {
    "real-time": "1715792818.122009",
    "sim-time": "94.598",
    "now drop rate": "5.220%",
    "now drop cnt": "439.143"
  },
  {
    "real-time": "1715792819.125249",
    "sim-time": "95.601",
    "now drop rate": "5.174%",
    "now drop cnt": "440.433"
  },
  {
    "real-time": "1715792820.127431",
    "sim-time": "96.604",
    "now drop rate": "5.129%",
    "now drop cnt": "441.711"
  },
  {
    "real-time": "1715792821.129762",
    "sim-time": "97.606",
    "now drop rate": "5.084%",
    "now drop cnt": "442.935"
  },
  {
    "real-time": "1715792822.133502",
    "sim-time": "98.610",
    "now drop rate": "5.042%",
    "now drop cnt": "444.331"
  },
  {
    "real-time": "1715792823.137088",
    "sim-time": "99.613",
    "now drop rate": "5.000%",
    "now drop cnt": "445.669"
  },
  {
    "real-time": "1715792824.140668",
    "sim-time": "100.617",
    "now drop rate": "4.959%",
    "now drop cnt": "447.026"
  },
  {
    "real-time": "1715792825.143190",
    "sim-time": "101.619",
    "now drop rate": "4.919%",
    "now drop cnt": "448.293"
  },
  {
    "real-time": "1715792826.145685",
    "sim-time": "102.622",
    "now drop rate": "4.878%",
    "now drop cnt": "449.524"
  },
  {
    "real-time": "1715792827.149580",
    "sim-time": "103.626",
    "now drop rate": "4.841%",
    "now drop cnt": "450.926"
  },
  {
    "real-time": "1715792828.152009",
    "sim-time": "104.628",
    "now drop rate": "4.803%",
    "now drop cnt": "452.194"
  },
  {
    "real-time": "1715792829.154787",
    "sim-time": "105.630",
    "now drop rate": "4.765%",
    "now drop cnt": "453.387"
  },
  {
    "real-time": "1715792830.157916",
    "sim-time": "106.634",
    "now drop rate": "4.729%",
    "now drop cnt": "454.756"
  },
  {
    "real-time": "1715792831.160971",
    "sim-time": "107.637",
    "now drop rate": "4.694%",
    "now drop cnt": "456.059"
  },
  {
    "real-time": "1715792832.164534",
    "sim-time": "108.641",
    "now drop rate": "4.660%",
    "now drop cnt": "457.414"
  },
  {
    "real-time": "1715792833.166909",
    "sim-time": "109.643",
    "now drop rate": "4.625%",
    "now drop cnt": "458.661"
  },
  {
    "drop rate": " 4.470%",
    "delay": " 160.833"
  }
]
data5 = [
  {
    "real-time": "1715793076.882714",
    "sim-time": "11.457",
    "now drop rate": "13.334%",
    "now drop cnt": "13.386"
  },
  {
    "real-time": "1715793077.885594",
    "sim-time": "12.460",
    "now drop rate": "7.306%",
    "now drop cnt": "14.660"
  },
  {
    "real-time": "1715793078.888884",
    "sim-time": "13.463",
    "now drop rate": "5.319%",
    "now drop cnt": "16.012"
  },
  {
    "real-time": "1715793079.891092",
    "sim-time": "14.465",
    "now drop rate": "4.289%",
    "now drop cnt": "17.206"
  },
  {
    "real-time": "1715793080.891868",
    "sim-time": "15.466",
    "now drop rate": "3.650%",
    "now drop cnt": "18.300"
  },
  {
    "real-time": "1715793081.892837",
    "sim-time": "16.467",
    "now drop rate": "3.226%",
    "now drop cnt": "19.402"
  },
  {
    "real-time": "1715793082.895069",
    "sim-time": "17.469",
    "now drop rate": "2.940%",
    "now drop cnt": "20.631"
  },
  {
    "real-time": "1715793083.898155",
    "sim-time": "18.472",
    "now drop rate": "2.736%",
    "now drop cnt": "21.937"
  },
  {
    "real-time": "1715793084.900831",
    "sim-time": "19.475",
    "now drop rate": "2.571%",
    "now drop cnt": "23.192"
  },
  {
    "real-time": "1715793085.906283",
    "sim-time": "20.480",
    "now drop rate": "2.467%",
    "now drop cnt": "24.740"
  },
  {
    "real-time": "1715793086.911115",
    "sim-time": "21.485",
    "now drop rate": "2.376%",
    "now drop cnt": "26.217"
  },
  {
    "real-time": "1715793087.913134",
    "sim-time": "22.487",
    "now drop rate": "2.279%",
    "now drop cnt": "27.430"
  },
  {
    "real-time": "1715793088.914809",
    "sim-time": "23.489",
    "now drop rate": "2.577%",
    "now drop cnt": "33.594"
  },
  {
    "real-time": "1715793089.917251",
    "sim-time": "24.491",
    "now drop rate": "2.482%",
    "now drop cnt": "34.837"
  },
  {
    "real-time": "1715793090.923990",
    "sim-time": "25.498",
    "now drop rate": "2.427%",
    "now drop cnt": "36.522"
  },
  {
    "real-time": "1715793092.073612",
    "sim-time": "26.658",
    "now drop rate": "3.547%",
    "now drop cnt": "57.481"
  },
  {
    "real-time": "1715793093.085063",
    "sim-time": "27.659",
    "now drop rate": "3.058%",
    "now drop cnt": "52.613"
  },
  {
    "real-time": "1715793094.089180",
    "sim-time": "28.663",
    "now drop rate": "2.966%",
    "now drop cnt": "54.015"
  },
  {
    "real-time": "1715793095.096428",
    "sim-time": "29.670",
    "now drop rate": "2.797%",
    "now drop cnt": "53.749"
  },
  {
    "real-time": "1715793096.098748",
    "sim-time": "30.673",
    "now drop rate": "2.720%",
    "now drop cnt": "55.000"
  },
  {
    "real-time": "1715793097.104070",
    "sim-time": "31.678",
    "now drop rate": "2.663%",
    "now drop cnt": "56.533"
  },
  {
    "real-time": "1715793098.107616",
    "sim-time": "32.682",
    "now drop rate": "2.604%",
    "now drop cnt": "57.880"
  },
  {
    "real-time": "1715793099.110599",
    "sim-time": "33.685",
    "now drop rate": "2.547%",
    "now drop cnt": "59.174"
  },
  {
    "real-time": "1715793100.120035",
    "sim-time": "34.695",
    "now drop rate": "3.309%",
    "now drop cnt": "80.225"
  },
  {
    "real-time": "1715793101.122345",
    "sim-time": "35.696",
    "now drop rate": "3.183%",
    "now drop cnt": "80.344"
  },
  {
    "real-time": "1715793102.124453",
    "sim-time": "36.698",
    "now drop rate": "3.106%",
    "now drop cnt": "81.509"
  },
  {
    "real-time": "1715793103.132684",
    "sim-time": "37.707",
    "now drop rate": "3.059%",
    "now drop cnt": "83.378"
  },
  {
    "real-time": "1715793104.137633",
    "sim-time": "38.712",
    "now drop rate": "3.003%",
    "now drop cnt": "84.866"
  },
  {
    "real-time": "1715793105.892811",
    "sim-time": "40.467",
    "now drop rate": "5.977%",
    "now drop cnt": "179.392"
  },
  {
    "real-time": "1715793106.896518",
    "sim-time": "41.471",
    "now drop rate": "5.699%",
    "now drop cnt": "176.771"
  },
  {
    "real-time": "1715793107.902998",
    "sim-time": "42.477",
    "now drop rate": "5.602%",
    "now drop cnt": "179.413"
  },
  {
    "real-time": "1715793108.905911",
    "sim-time": "43.487",
    "now drop rate": "5.490%",
    "now drop cnt": "181.366"
  },
  {
    "real-time": "1715793109.915148",
    "sim-time": "44.489",
    "now drop rate": "5.364%",
    "now drop cnt": "182.561"
  },
  {
    "real-time": "1715793110.917959",
    "sim-time": "45.492",
    "now drop rate": "5.249%",
    "now drop cnt": "183.902"
  },
  {
    "real-time": "1715793111.921289",
    "sim-time": "46.495",
    "now drop rate": "5.139%",
    "now drop cnt": "185.238"
  },
  {
    "real-time": "1715793112.927371",
    "sim-time": "47.501",
    "now drop rate": "5.043%",
    "now drop cnt": "186.848"
  },
  {
    "real-time": "1715793113.929660",
    "sim-time": "48.504",
    "now drop rate": "4.943%",
    "now drop cnt": "188.071"
  },
  {
    "real-time": "1715793114.930352",
    "sim-time": "49.504",
    "now drop rate": "4.946%",
    "now drop cnt": "193.149"
  },
  {
    "real-time": "1715793115.933297",
    "sim-time": "50.507",
    "now drop rate": "4.855%",
    "now drop cnt": "194.447"
  },
  {
    "real-time": "1715793116.936432",
    "sim-time": "51.511",
    "now drop rate": "4.770%",
    "now drop cnt": "195.830"
  },
  {
    "real-time": "1715793117.945580",
    "sim-time": "52.520",
    "now drop rate": "4.699%",
    "now drop cnt": "197.662"
  },
  {
    "real-time": "1715793118.950916",
    "sim-time": "53.525",
    "now drop rate": "4.602%",
    "now drop cnt": "198.217"
  },
  {
    "real-time": "1715793119.956090",
    "sim-time": "54.530",
    "now drop rate": "4.531%",
    "now drop cnt": "199.733"
  },
  {
    "real-time": "1715793120.960298",
    "sim-time": "55.534",
    "now drop rate": "4.439%",
    "now drop cnt": "200.139"
  },
  {
    "real-time": "1715793121.964938",
    "sim-time": "56.539",
    "now drop rate": "4.375%",
    "now drop cnt": "201.616"
  },
  {
    "real-time": "1715793122.967401",
    "sim-time": "57.541",
    "now drop rate": "4.307%",
    "now drop cnt": "202.827"
  },
  {
    "real-time": "1715793123.969541",
    "sim-time": "58.544",
    "now drop rate": "4.245%",
    "now drop cnt": "204.143"
  },
  {
    "real-time": "1715793124.972155",
    "sim-time": "59.546",
    "now drop rate": "4.203%",
    "now drop cnt": "206.326"
  },
  {
    "real-time": "1715793125.975237",
    "sim-time": "60.549",
    "now drop rate": "4.304%",
    "now drop cnt": "215.613"
  },
  {
    "real-time": "1715793126.980120",
    "sim-time": "61.554",
    "now drop rate": "4.249%",
    "now drop cnt": "217.126"
  },
  {
    "real-time": "1715793127.982628",
    "sim-time": "62.557",
    "now drop rate": "4.191%",
    "now drop cnt": "218.381"
  },
  {
    "real-time": "1715793128.985039",
    "sim-time": "63.558",
    "now drop rate": "4.208%",
    "now drop cnt": "223.485"
  },
  {
    "real-time": "1715793129.988589",
    "sim-time": "64.563",
    "now drop rate": "4.158%",
    "now drop cnt": "224.966"
  },
  {
    "real-time": "1715793130.991439",
    "sim-time": "65.566",
    "now drop rate": "4.105%",
    "now drop cnt": "226.251"
  },
  {
    "real-time": "1715793131.995772",
    "sim-time": "66.570",
    "now drop rate": "4.057%",
    "now drop cnt": "227.681"
  },
  {
    "real-time": "1715793132.998706",
    "sim-time": "67.573",
    "now drop rate": "4.026%",
    "now drop cnt": "229.982"
  },
  {
    "real-time": "1715793134.003471",
    "sim-time": "68.577",
    "now drop rate": "3.982%",
    "now drop cnt": "231.439"
  },
  {
    "real-time": "1715793135.009341",
    "sim-time": "69.584",
    "now drop rate": "3.891%",
    "now drop cnt": "230.053"
  },
  {
    "real-time": "1715793136.011645",
    "sim-time": "70.586",
    "now drop rate": "3.846%",
    "now drop cnt": "231.267"
  },
  {
    "real-time": "1715793137.020539",
    "sim-time": "71.595",
    "now drop rate": "4.141%",
    "now drop cnt": "253.164"
  },
  {
    "real-time": "1715793138.024935",
    "sim-time": "72.599",
    "now drop rate": "4.097%",
    "now drop cnt": "254.620"
  },
  {
    "real-time": "1715793139.886129",
    "sim-time": "74.460",
    "now drop rate": "5.448%",
    "now drop cnt": "348.743"
  },
  {
    "real-time": "1715793140.889607",
    "sim-time": "75.464",
    "now drop rate": "5.385%",
    "now drop cnt": "350.071"
  },
  {
    "real-time": "1715793141.898257",
    "sim-time": "76.472",
    "now drop rate": "5.331%",
    "now drop cnt": "351.922"
  },
  {
    "real-time": "1715793143.456314",
    "sim-time": "78.041",
    "now drop rate": "6.151%",
    "now drop cnt": "415.754"
  },
  {
    "real-time": "1715793144.472751",
    "sim-time": "79.047",
    "now drop rate": "5.108%",
    "now drop cnt": "350.377"
  },
  {
    "real-time": "1715793145.474563",
    "sim-time": "80.049",
    "now drop rate": "5.612%",
    "now drop cnt": "390.566"
  },
  {
    "real-time": "1715793146.477966",
    "sim-time": "81.052",
    "now drop rate": "5.551%",
    "now drop cnt": "391.911"
  },
  {
    "real-time": "1715793147.481779",
    "sim-time": "82.056",
    "now drop rate": "5.493%",
    "now drop cnt": "393.283"
  },
  {
    "real-time": "1715793148.484884",
    "sim-time": "83.059",
    "now drop rate": "5.435%",
    "now drop cnt": "394.607"
  },
  {
    "real-time": "1715793149.488194",
    "sim-time": "84.062",
    "now drop rate": "5.379%",
    "now drop cnt": "395.941"
  },
  {
    "real-time": "1715793150.492264",
    "sim-time": "85.066",
    "now drop rate": "5.325%",
    "now drop cnt": "397.330"
  },
  {
    "real-time": "1715793151.495776",
    "sim-time": "86.070",
    "now drop rate": "5.273%",
    "now drop cnt": "398.709"
  },
  {
    "real-time": "1715793152.500525",
    "sim-time": "87.075",
    "now drop rate": "5.210%",
    "now drop cnt": "399.163"
  },
  {
    "real-time": "1715793153.503017",
    "sim-time": "88.077",
    "now drop rate": "5.158%",
    "now drop cnt": "400.410"
  },
  {
    "real-time": "1715793154.506019",
    "sim-time": "89.080",
    "now drop rate": "5.109%",
    "now drop cnt": "401.701"
  },
  {
    "real-time": "1715793155.510620",
    "sim-time": "90.085",
    "now drop rate": "5.063%",
    "now drop cnt": "403.183"
  },
  {
    "real-time": "1715793156.512546",
    "sim-time": "91.087",
    "now drop rate": "5.015%",
    "now drop cnt": "404.365"
  },
  {
    "real-time": "1715793157.514355",
    "sim-time": "92.088",
    "now drop rate": "4.968%",
    "now drop cnt": "405.548"
  },
  {
    "real-time": "1715793158.516042",
    "sim-time": "93.090",
    "now drop rate": "4.922%",
    "now drop cnt": "406.731"
  },
  {
    "real-time": "1715793159.519437",
    "sim-time": "94.093",
    "now drop rate": "4.879%",
    "now drop cnt": "408.043"
  },
  {
    "real-time": "1715793160.523898",
    "sim-time": "95.098",
    "now drop rate": "4.838%",
    "now drop cnt": "409.495"
  },
  {
    "real-time": "1715793161.525475",
    "sim-time": "96.100",
    "now drop rate": "4.795%",
    "now drop cnt": "410.657"
  },
  {
    "real-time": "1715793162.526596",
    "sim-time": "97.101",
    "now drop rate": "4.752%",
    "now drop cnt": "411.777"
  },
  {
    "real-time": "1715793163.529095",
    "sim-time": "98.103",
    "now drop rate": "4.712%",
    "now drop cnt": "413.017"
  },
  {
    "real-time": "1715793164.532930",
    "sim-time": "99.107",
    "now drop rate": "4.674%",
    "now drop cnt": "414.392"
  },
  {
    "real-time": "1715793165.539424",
    "sim-time": "100.114",
    "now drop rate": "4.640%",
    "now drop cnt": "416.053"
  },
  {
    "real-time": "1715793166.542434",
    "sim-time": "101.116",
    "now drop rate": "4.614%",
    "now drop cnt": "418.347"
  },
  {
    "real-time": "1715793167.549221",
    "sim-time": "102.123",
    "now drop rate": "4.582%",
    "now drop cnt": "420.032"
  },
  {
    "real-time": "1715793168.553310",
    "sim-time": "103.127",
    "now drop rate": "4.547%",
    "now drop cnt": "421.436"
  },
  {
    "real-time": "1715793169.558243",
    "sim-time": "104.132",
    "now drop rate": "4.515%",
    "now drop cnt": "422.937"
  },
  {
    "real-time": "1715793170.561650",
    "sim-time": "105.136",
    "now drop rate": "4.481%",
    "now drop cnt": "424.274"
  },
  {
    "real-time": "1715793171.563456",
    "sim-time": "106.138",
    "now drop rate": "4.447%",
    "now drop cnt": "425.476"
  },
  {
    "real-time": "1715793172.565593",
    "sim-time": "107.140",
    "now drop rate": "4.413%",
    "now drop cnt": "426.660"
  },
  {
    "real-time": "1715793173.567124",
    "sim-time": "108.141",
    "now drop rate": "4.380%",
    "now drop cnt": "427.839"
  },
  {
    "real-time": "1715793174.577309",
    "sim-time": "109.151",
    "now drop rate": "4.365%",
    "now drop cnt": "430.840"
  },
  {
    "real-time": "1715793175.579311",
    "sim-time": "110.154",
    "now drop rate": "4.344%",
    "now drop cnt": "433.119"
  },
  {
    "drop rate": " 4.210%",
    "delay": " 164.864"
  }
]


labels = ['1st test', '2nd test', '3rd test', '4th test', '5th test']

for i, data in enumerate([data1, data2, data3, data4, data5]):
    time_points = [float(d['sim-time'].strip()) for d in data[:-1]]
    drop_rates = [float(d['now drop cnt']) for d in data[:-1]]
    plt.plot(time_points, drop_rates, label=labels[i])

plt.xlabel('time (s)')
plt.ylabel('packet drop rate')
plt.title('66 satellites, 5% failure, n=5, packet drop rate over time')
# plt.xlim(0, 100)
# plt.ylim(0, 23.5)

# plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())

plt.legend()
plt.grid()
plt.show()