import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
data = [
  {
    "real-time": "1714118909.039144",
    "sim-time": "11.437",
    "now drop rate": "7.920%",
    "now drop cnt": "7.999"
  },
  {
    "real-time": "1714118910.041607",
    "sim-time": "12.439",
    "now drop rate": "4.595%",
    "now drop cnt": "9.248"
  },
  {
    "real-time": "1714118911.043478",
    "sim-time": "13.441",
    "now drop rate": "3.459%",
    "now drop cnt": "10.425"
  },
  {
    "real-time": "1714118912.046979",
    "sim-time": "14.445",
    "now drop rate": "2.936%",
    "now drop cnt": "11.797"
  },
  {
    "real-time": "1714118913.047985",
    "sim-time": "15.445",
    "now drop rate": "2.567%",
    "now drop cnt": "12.883"
  },
  {
    "real-time": "1714118914.049702",
    "sim-time": "16.447",
    "now drop rate": "2.334%",
    "now drop cnt": "14.052"
  },
  {
    "real-time": "1714118915.051625",
    "sim-time": "17.449",
    "now drop rate": "2.174%",
    "now drop cnt": "15.266"
  },
  {
    "real-time": "1714118916.055728",
    "sim-time": "18.453",
    "now drop rate": "2.076%",
    "now drop cnt": "16.667"
  },
  {
    "real-time": "1714118917.058621",
    "sim-time": "19.456",
    "now drop rate": "1.988%",
    "now drop cnt": "17.952"
  },
  {
    "real-time": "1714118918.061336",
    "sim-time": "20.459",
    "now drop rate": "1.917%",
    "now drop cnt": "19.232"
  },
  {
    "real-time": "1714118919.066358",
    "sim-time": "21.464",
    "now drop rate": "1.877%",
    "now drop cnt": "20.717"
  },
  {
    "real-time": "1714118920.068297",
    "sim-time": "22.466",
    "now drop rate": "1.821%",
    "now drop cnt": "21.918"
  },
  {
    "real-time": "1714118921.070276",
    "sim-time": "23.468",
    "now drop rate": "2.157%",
    "now drop cnt": "28.127"
  },
  {
    "real-time": "1714118922.072840",
    "sim-time": "24.470",
    "now drop rate": "2.092%",
    "now drop cnt": "29.374"
  },
  {
    "real-time": "1714118923.081043",
    "sim-time": "25.478",
    "now drop rate": "2.072%",
    "now drop cnt": "31.183"
  },
  {
    "real-time": "1714118924.088838",
    "sim-time": "26.486",
    "now drop rate": "2.114%",
    "now drop cnt": "33.944"
  },
  {
    "real-time": "1714118925.088619",
    "sim-time": "27.486",
    "now drop rate": "3.398%",
    "now drop cnt": "57.967"
  },
  {
    "real-time": "1714118926.090716",
    "sim-time": "28.488",
    "now drop rate": "3.276%",
    "now drop cnt": "59.164"
  },
  {
    "real-time": "1714118927.097350",
    "sim-time": "29.495",
    "now drop rate": "3.190%",
    "now drop cnt": "60.827"
  },
  {
    "real-time": "1714118928.097992",
    "sim-time": "30.496",
    "now drop rate": "3.084%",
    "now drop cnt": "61.894"
  },
  {
    "real-time": "1714118929.101728",
    "sim-time": "31.499",
    "now drop rate": "3.003%",
    "now drop cnt": "63.274"
  },
  {
    "real-time": "1714118930.110794",
    "sim-time": "32.508",
    "now drop rate": "2.951%",
    "now drop cnt": "65.173"
  },
  {
    "real-time": "1714118931.111973",
    "sim-time": "33.510",
    "now drop rate": "2.872%",
    "now drop cnt": "66.287"
  },
  {
    "real-time": "1714118935.345614",
    "sim-time": "36.835",
    "now drop rate": "13.892%",
    "now drop cnt": "366.872"
  },
  {
    "real-time": "1714118935.439958",
    "sim-time": "37.839",
    "now drop rate": "13.726%",
    "now drop cnt": "376.282"
  },
  {
    "real-time": "1714118936.443534",
    "sim-time": "38.841",
    "now drop rate": "13.284%",
    "now drop cnt": "377.457"
  },
  {
    "real-time": "1714118937.449210",
    "sim-time": "39.846",
    "now drop rate": "12.882%",
    "now drop cnt": "378.975"
  },
  {
    "real-time": "1714118938.450754",
    "sim-time": "40.848",
    "now drop rate": "12.497%",
    "now drop cnt": "380.180"
  },
  {
    "real-time": "1714118939.459264",
    "sim-time": "41.857",
    "now drop rate": "12.091%",
    "now drop cnt": "380.013"
  },
  {
    "real-time": "1714118940.460912",
    "sim-time": "42.859",
    "now drop rate": "11.754%",
    "now drop cnt": "381.192"
  },
  {
    "real-time": "1714118941.462570",
    "sim-time": "43.860",
    "now drop rate": "11.436%",
    "now drop cnt": "382.347"
  },
  {
    "real-time": "1714118942.466503",
    "sim-time": "44.864",
    "now drop rate": "11.143%",
    "now drop cnt": "383.746"
  },
  {
    "real-time": "1714118943.471702",
    "sim-time": "45.869",
    "now drop rate": "10.870%",
    "now drop cnt": "385.267"
  },
  {
    "real-time": "1714118944.475394",
    "sim-time": "46.873",
    "now drop rate": "10.609%",
    "now drop cnt": "386.645"
  },
  {
    "real-time": "1714118945.477249",
    "sim-time": "47.875",
    "now drop rate": "10.356%",
    "now drop cnt": "387.821"
  },
  {
    "real-time": "1714118946.483487",
    "sim-time": "48.881",
    "now drop rate": "10.153%",
    "now drop cnt": "390.438"
  },
  {
    "real-time": "1714118947.485507",
    "sim-time": "49.883",
    "now drop rate": "9.926%",
    "now drop cnt": "391.642"
  },
  {
    "real-time": "1714118948.488616",
    "sim-time": "50.886",
    "now drop rate": "9.712%",
    "now drop cnt": "392.950"
  },
  {
    "real-time": "1714118949.489619",
    "sim-time": "51.887",
    "now drop rate": "9.504%",
    "now drop cnt": "394.047"
  },
  {
    "real-time": "1714118950.491888",
    "sim-time": "52.889",
    "now drop rate": "9.309%",
    "now drop cnt": "395.266"
  },
  {
    "real-time": "1714118951.492834",
    "sim-time": "53.893",
    "now drop rate": "9.170%",
    "now drop cnt": "398.590"
  },
  {
    "real-time": "1714118952.504874",
    "sim-time": "54.903",
    "now drop rate": "8.984%",
    "now drop cnt": "399.593"
  },
  {
    "real-time": "1714118953.505963",
    "sim-time": "55.903",
    "now drop rate": "8.811%",
    "now drop cnt": "400.684"
  },
  {
    "real-time": "1714118954.509280",
    "sim-time": "56.907",
    "now drop rate": "8.649%",
    "now drop cnt": "402.024"
  },
  {
    "real-time": "1714118955.511340",
    "sim-time": "57.909",
    "now drop rate": "8.492%",
    "now drop cnt": "403.226"
  },
  {
    "real-time": "1714118956.514356",
    "sim-time": "58.912",
    "now drop rate": "8.344%",
    "now drop cnt": "404.539"
  },
  {
    "real-time": "1714118957.516155",
    "sim-time": "59.917",
    "now drop rate": "8.204%",
    "now drop cnt": "406.035"
  },
  {
    "real-time": "1714118958.519786",
    "sim-time": "60.917",
    "now drop rate": "8.062%",
    "now drop cnt": "407.068"
  },
  {
    "real-time": "1714118959.522327",
    "sim-time": "61.920",
    "now drop rate": "7.930%",
    "now drop cnt": "408.338"
  },
  {
    "real-time": "1714118960.531205",
    "sim-time": "62.929",
    "now drop rate": "7.870%",
    "now drop cnt": "413.217"
  },
  {
    "real-time": "1714118961.533500",
    "sim-time": "63.931",
    "now drop rate": "7.746%",
    "now drop cnt": "414.437"
  },
  {
    "real-time": "1714118962.534812",
    "sim-time": "64.932",
    "now drop rate": "7.624%",
    "now drop cnt": "415.576"
  },
  {
    "real-time": "1714118963.544488",
    "sim-time": "65.942",
    "now drop rate": "7.449%",
    "now drop cnt": "413.557"
  },
  {
    "real-time": "1714118964.550688",
    "sim-time": "66.948",
    "now drop rate": "7.345%",
    "now drop cnt": "415.168"
  },
  {
    "real-time": "1714118965.553622",
    "sim-time": "67.951",
    "now drop rate": "7.240%",
    "now drop cnt": "416.454"
  },
  {
    "real-time": "1714118966.556223",
    "sim-time": "68.954",
    "now drop rate": "7.137%",
    "now drop cnt": "417.710"
  },
  {
    "real-time": "1714118967.562559",
    "sim-time": "69.960",
    "now drop rate": "7.044%",
    "now drop cnt": "419.347"
  },
  {
    "real-time": "1714118968.564259",
    "sim-time": "70.962",
    "now drop rate": "7.012%",
    "now drop cnt": "424.499"
  },
  {
    "real-time": "1714118969.565682",
    "sim-time": "71.963",
    "now drop rate": "6.917%",
    "now drop cnt": "425.670"
  },
  {
    "real-time": "1714118970.568515",
    "sim-time": "72.966",
    "now drop rate": "6.826%",
    "now drop cnt": "426.915"
  },
  {
    "real-time": "1714118971.571338",
    "sim-time": "73.969",
    "now drop rate": "6.739%",
    "now drop cnt": "428.213"
  },
  {
    "real-time": "1714118972.574339",
    "sim-time": "74.972",
    "now drop rate": "6.654%",
    "now drop cnt": "429.513"
  },
  {
    "real-time": "1714118973.576008",
    "sim-time": "75.974",
    "now drop rate": "6.571%",
    "now drop cnt": "430.730"
  },
  {
    "real-time": "1714118974.578760",
    "sim-time": "76.976",
    "now drop rate": "6.476%",
    "now drop cnt": "430.971"
  },
  {
    "real-time": "1714118975.584255",
    "sim-time": "77.982",
    "now drop rate": "6.403%",
    "now drop cnt": "432.536"
  },
  {
    "real-time": "1714118976.587615",
    "sim-time": "78.985",
    "now drop rate": "6.328%",
    "now drop cnt": "433.864"
  },
  {
    "real-time": "1714118977.596246",
    "sim-time": "79.994",
    "now drop rate": "6.321%",
    "now drop cnt": "439.757"
  },
  {
    "real-time": "1714118978.605043",
    "sim-time": "81.003",
    "now drop rate": "6.257%",
    "now drop cnt": "441.600"
  },
  {
    "real-time": "1714118979.606397",
    "sim-time": "82.004",
    "now drop rate": "6.185%",
    "now drop cnt": "442.738"
  },
  {
    "real-time": "1714118980.608045",
    "sim-time": "83.006",
    "now drop rate": "6.116%",
    "now drop cnt": "443.892"
  },
  {
    "real-time": "1714118981.609128",
    "sim-time": "84.007",
    "now drop rate": "6.048%",
    "now drop cnt": "445.008"
  },
  {
    "real-time": "1714118982.610517",
    "sim-time": "85.008",
    "now drop rate": "5.969%",
    "now drop cnt": "445.149"
  },
  {
    "real-time": "1714118983.613300",
    "sim-time": "86.011",
    "now drop rate": "5.880%",
    "now drop cnt": "444.425"
  },
  {
    "real-time": "1714118984.617320",
    "sim-time": "87.015",
    "now drop rate": "5.821%",
    "now drop cnt": "445.824"
  },
  {
    "real-time": "1714118985.618084",
    "sim-time": "88.016",
    "now drop rate": "5.760%",
    "now drop cnt": "446.898"
  },
  {
    "real-time": "1714118986.619713",
    "sim-time": "89.017",
    "now drop rate": "5.701%",
    "now drop cnt": "448.074"
  },
  {
    "real-time": "1714118987.620517",
    "sim-time": "90.018",
    "now drop rate": "5.643%",
    "now drop cnt": "449.150"
  },
  {
    "real-time": "1714118988.621943",
    "sim-time": "91.019",
    "now drop rate": "5.587%",
    "now drop cnt": "450.280"
  },
  {
    "real-time": "1714118989.624960",
    "sim-time": "92.024",
    "now drop rate": "5.536%",
    "now drop cnt": "451.722"
  },
  {
    "real-time": "1714118990.627318",
    "sim-time": "93.025",
    "now drop rate": "5.482%",
    "now drop cnt": "452.836"
  },
  {
    "real-time": "1714118991.628139",
    "sim-time": "94.026",
    "now drop rate": "5.430%",
    "now drop cnt": "453.904"
  },
  {
    "real-time": "1714118992.630110",
    "sim-time": "95.028",
    "now drop rate": "5.379%",
    "now drop cnt": "455.107"
  },
  {
    "real-time": "1714118993.639489",
    "sim-time": "96.037",
    "now drop rate": "5.327%",
    "now drop cnt": "456.045"
  },
  {
    "real-time": "1714118994.639806",
    "sim-time": "97.037",
    "now drop rate": "5.277%",
    "now drop cnt": "457.079"
  },
  {
    "real-time": "1714118995.641489",
    "sim-time": "98.039",
    "now drop rate": "5.230%",
    "now drop cnt": "458.237"
  },
  {
    "real-time": "1714118996.647413",
    "sim-time": "99.045",
    "now drop rate": "5.189%",
    "now drop cnt": "459.860"
  },
  {
    "real-time": "1714118997.653840",
    "sim-time": "100.051",
    "now drop rate": "5.149%",
    "now drop cnt": "461.480"
  },
  {
    "real-time": "1714118998.656611",
    "sim-time": "101.054",
    "now drop rate": "5.106%",
    "now drop cnt": "462.758"
  },
  {
    "real-time": "1714118999.660592",
    "sim-time": "102.058",
    "now drop rate": "5.065%",
    "now drop cnt": "464.154"
  },
  {
    "real-time": "1714119000.664014",
    "sim-time": "103.062",
    "now drop rate": "5.025%",
    "now drop cnt": "465.502"
  },
  {
    "real-time": "1714119001.665864",
    "sim-time": "104.063",
    "now drop rate": "4.984%",
    "now drop cnt": "466.674"
  },
  {
    "real-time": "1714119002.668208",
    "sim-time": "105.066",
    "now drop rate": "4.944%",
    "now drop cnt": "467.916"
  },
  {
    "real-time": "1714119003.668716",
    "sim-time": "106.066",
    "now drop rate": "4.904%",
    "now drop cnt": "468.970"
  },
  {
    "real-time": "1714119004.670821",
    "sim-time": "107.068",
    "now drop rate": "4.865%",
    "now drop cnt": "470.173"
  },
  {
    "real-time": "1714119005.671476",
    "sim-time": "108.069",
    "now drop rate": "4.826%",
    "now drop cnt": "471.240"
  },
  {
    "real-time": "1714119006.677018",
    "sim-time": "109.075",
    "now drop rate": "4.803%",
    "now drop cnt": "473.805"
  },
  {
    "real-time": "1714119007.679110",
    "sim-time": "110.077",
    "now drop rate": "4.767%",
    "now drop cnt": "475.008"
  },
  {
    "drop rate": " 4.690%",
    "delay": " 109.130"
  }
]


sim_time_points = [float(d['sim-time'].strip()) for d in data[:-1]]
real_time_points = [float(d['real-time'].strip()) for d in data[:-1]]
drop_cnts = [float(d['now drop cnt']) for d in data[:-1]]
ttl_drop_cnts = []


with open(f'{current_directory}/kernel.txt', 'r') as f:
	lines = f.readlines()
	j = 0
	ttl_drop_cnt = 0
	for i in range(len(real_time_points)):
		real_time = real_time_points[i]
		while j < len(lines):
			ttl_real_time = float(lines[j].strip().split("]")[0][1:])
			if ttl_real_time <= real_time:
				ttl_drop_cnt += 1
				j += 1
			else:
				break
		ttl_drop_cnts.append(ttl_drop_cnt)

plt.plot(sim_time_points, ttl_drop_cnts, label='ttl drop cnt')
plt.plot(sim_time_points, drop_cnts, label='total drop cnt')


plt.fill_between(sim_time_points, ttl_drop_cnts, 0, color='C0', alpha=0.3)
plt.fill_between(sim_time_points, drop_cnts, ttl_drop_cnts, color='C1', alpha=0.3)

plt.xlabel('time (s)')
plt.ylabel('packet drop cnt')
plt.title('66 satellites, 5% failure, n=2, packet drop cnt over time')
plt.xlim(10, 110)
plt.ylim(0, 800)

# plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())

plt.legend()
plt.grid()
plt.show()