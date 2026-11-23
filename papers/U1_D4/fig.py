import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
navy="#0A2444"; blue="#2F6DB5"; grey="#7A8594"
b8=[0.585,0.595,0.605,0.610,0.615,0.625,0.635]
hot=[0.57780,0.55391,0.52209,0.49710,0.40838,0.38587,0.37029]; cold=[0.57817,0.55459,0.52101,0.50193,0.40808,0.38599,0.37048]
m12=([0.605,0.6075,0.610,0.6125,0.615,0.6175,0.620],[0.52330,0.51235,0.49981,0.48119,0.41193,0.40082,0.39665])
m16=([0.60875,0.61125,0.61375,0.61625,0.61875],[0.50497,0.49101,0.46668,0.40573,0.39934])
fig,ax=plt.subplots(1,2,figsize=(6.8,2.7),sharey=True)
ax[0].plot(b8,hot,"o-",color=navy,ms=4,lw=1,label="hot start"); ax[0].plot(b8,cold,"s--",color=blue,ms=4,lw=1,mfc="none",label="cold start")
ax[0].set_xlabel(r"$\beta$"); ax[0].set_ylabel(r"$E=\langle 1-\cos\theta_\triangle\rangle$"); ax[0].set_title(r"(a) $L=8$, thermal scans",fontsize=9); ax[0].legend(frameon=False,fontsize=8)
ax[1].plot(*m12,"o-",color=navy,ms=4,lw=1,label=r"$L=12$"); ax[1].plot(*m16,"D-",color=blue,ms=4,lw=1,label=r"$L=16$")
ax[1].axhspan(0.44482,0.46482,color=grey,alpha=0.25,lw=0); ax[1].axvline(0.6150,color=grey,lw=0.8,ls=":")
ax[1].set_xlabel(r"$\beta$"); ax[1].set_title("(b) mixed starts, last 500 sweeps",fontsize=9); ax[1].legend(frameon=False,fontsize=8)
for a in ax: a.tick_params(labelsize=8)
ax[0].set_xticks([0.59,0.61,0.63]); ax[1].set_xticks([0.605,0.610,0.615,0.620])
plt.tight_layout(); plt.savefig("fig1.pdf")
