import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import os
import json

current_directory = os.path.dirname(os.path.abspath(__file__))
with open(f"{current_directory}/long_term_result.json", 'r') as f:
	data = json.load(f)


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
plt.title('66 satellites, 5% failure, n=5, packet drop cnt over time')
plt.xlim(10, 110)
plt.ylim(0, 800)

# plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())

plt.legend()
plt.grid()
plt.show()