import skrf as rf
import matplotlib.pyplot as plt


def show_plot(filename, title_through="S21", title_ret = "S11"):
	ntwk = rf.Network(filename)

	# Convert frequency from Hz to GHz for plotting
	freq_ghz = ntwk.f / 1e9

	# Create a figure and 2 side-by-side subplots
	fig, (ax_s21, ax_s11) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

	# --------------------------
	# Subplot 1: S21
	# --------------------------
	ax_s21_phase = ax_s21.twinx()  # second y-axis for phase

	# Plot S21 magnitude (dB) on the left y-axis
	mag_s21 = ntwk.s21.s_db.flatten()
	ax_s21.plot(freq_ghz, mag_s21, label=f"{title_through} |dB|")
	ax_s21.set_xlabel("Frequency (GHz)")
	ax_s21.set_ylabel("Magnitude (dB)")

	# Plot S21 phase (degrees) on the right y-axis
	phase_s21 = ntwk.s21.s_deg.flatten()
	ax_s21_phase.plot(freq_ghz, phase_s21, label=f"{title_through} Phase (deg)", linestyle="--", color="orange")
	ax_s21_phase.set_ylabel("Phase (degrees)")

	# Combine legends for magnitude and phase in the first subplot
	lines1, labels1 = ax_s21.get_legend_handles_labels()
	lines2, labels2 = ax_s21_phase.get_legend_handles_labels()
	ax_s21.legend(lines1 + lines2, labels1 + labels2, loc="best")

	ax_s21.set_title(f"{title_through} Magnitude & Phase")

	# --------------------------
	# Subplot 2: S11
	# --------------------------
	ax_s11_phase = ax_s11.twinx()  # second y-axis for phase

	# Plot S11 magnitude (dB) on the left y-axis
	mag_s11 = ntwk.s11.s_db.flatten()
	ax_s11.plot(freq_ghz, mag_s11, label=f"{title_ret} |dB|")
	ax_s11.set_xlabel("Frequency (GHz)")
	ax_s11.set_ylabel("Magnitude (dB)")

	# Plot S11 phase (degrees) on the right y-axis
	phase_s11 = ntwk.s11.s_deg.flatten()
	ax_s11_phase.plot(freq_ghz, phase_s11, label=f"{title_ret} Phase (deg)", linestyle="--", color="orange")
	ax_s11_phase.set_ylabel("Phase (degrees)")

	# Combine legends for magnitude and phase in the second subplot
	lines3, labels3 = ax_s11.get_legend_handles_labels()
	lines4, labels4 = ax_s11_phase.get_legend_handles_labels()
	ax_s11.legend(lines3 + lines4, labels3 + labels4, loc="best")

	ax_s11.set_title(f"{title_ret} Magnitude & Phase")

	plt.tight_layout()
	plt.show()


def show_filtered_networks(filtered_networks, Vce, Ic):
	ro_ns = rf.NetworkSet(filtered_networks, name='ro set')
	noiseless_dict =  {k: v for k, v in filtered_networks.items() if k[2] == 0}
	ro_ns_noiseless = rf.NetworkSet(noiseless_dict, name ='noiseless set')
	noisy_dict =  {k: v for k, v in filtered_networks.items() if k[2]}
	ro_ns_noisy= rf.NetworkSet(noisy_dict, name ='noisy set')
	vce_const_dict = {k: v for k, v in filtered_networks.items() if k[0] == Vce}
	ro_ns_vce_1V= rf.NetworkSet(vce_const_dict, name =f'vce:{Vce}V')
	ic_const_dict = {k: v for k, v in filtered_networks.items() if k[1] == Ic}
	ro_ns_ic_42mA= rf.NetworkSet(ic_const_dict, name =f'Ic:{Ic}mA')

	fig = plt.figure(figsize=(9,8))
	ax1 = fig.add_subplot(221)
	ax2 = fig.add_subplot(222); ax2.grid()
	ax3 = fig.add_subplot(223)
	ax4 = fig.add_subplot(224); ax4.grid()

	ro_ns_noiseless.plot_uncertainty_bounds_s_db(ax=ax1)
	ro_ns_noisy.plot_uncertainty_bounds_s_db(ax=ax2)
	ro_ns_vce_1V.plot_uncertainty_bounds_s_db(ax=ax3)
	ro_ns_ic_42mA.plot_uncertainty_bounds_s_db(ax=ax4)
	fig.tight_layout()
	plt.show()
	ro_ns.plot_uncertainty_bounds_s_db()
	plt.show()