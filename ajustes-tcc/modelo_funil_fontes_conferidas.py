M=["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
new=[50,30,60,35,35,35,35,40,40,45,65,30]
sub=[35,21,42,25,24,25,24,28,28,32,45,21]
av=[n-s for n,s in zip(new,sub)]
P1,P2=179.99,145.99
ads=[3528,2117,4234,2470,2470,2470,2470,2822,2822,3175,4586,2116]
seo=[30,50,80,120,170,230,300,380,460,540,620,700]
def f(x,d=0): return f"{x:,.{d}f}".replace(",","X").replace(".",",").replace("X",".")
def run(ren,rep):
    perm=[1,1,1,ren,ren,ren,ren**2,ren**2,ren**2,ren**3,ren**3,ren**3]
    act=[sum(sub[c]*perm[m-c] for c in range(m+1)) for m in range(12)]
    rec=[0,0]+[rep*av[m-2] for m in range(2,12)]
    box=[act[m]+av[m]+rec[m] for m in range(12)]
    rev=sum(act)*P2+(sum(av)+sum(rec))*P1
    contrib=sum(act)*P2*.17+(sum(av)+sum(rec))*P1*.31
    recur=(sum(box)-500)/sum(box)
    avgperm=sum(perm)
    return dict(box=sum(box),rev=rev,recur=recur,dec=act[11],coh=perm[11],ltvcac=contrib/500/252.8,contrib=contrib,avgperm=avgperm)
for name,conv,ab,cpc,ren,rep in [("pess",.0075,.80,3,.4,.15),("real",.0109,.80,2,.5,.2),("otim",.0158,.7022,1,.7,.3)]:
    r=run(ren,rep); vis=500/conv; paid=35280/cpc; carts=500/(1-ab)
    print(name, "vis",f(vis),"paid",f(paid),"rest",f(max(vis-paid,0)),f(max(vis-paid,0)/vis*100),"% carts",f(carts),"aband",f(carts-500),
      "box",f(r['box']),"rev",f(r['rev']),"recur",f(r['recur']*100),"dec",f(r['dec']),"coh",f(r['coh']*100),"ltvcac",f(r['ltvcac'],2),"perm",f(r['avgperm'],1))
# monthly realista funnel
conv=.0109
rows=["| Mês | Pedidos de novas clientes | Visitas necessárias | Carrinhos criados | Carrinhos abandonados |","| --- | --- | --- | --- | --- |"]
rows2=["| Mês | Total de visitas | Anúncios pagos | Influência e parcerias | Redes orgânicas | Busca (SEO) | Direto, e-mail e lista |","| --- | --- | --- | --- | --- | --- | --- |"]
T=[0]*7
for m in range(12):
    v=new[m]/conv; c=new[m]/.2
    p=ads[m]/2; d=v*.05; s=seo[m]; rest=v-p-d-s
    i=rest/2; o=rest/2
    rows.append(f"| {M[m]}/27 | {new[m]} | {f(v)} | {f(c)} | {f(c-new[m])} |")
    rows2.append(f"| {M[m]}/27 | {f(v)} | {f(p)} | {f(i)} | {f(o)} | {f(s)} | {f(d)} |")
    for k,x in enumerate([v,p,i,o,s,d]): T[k]+=x
rows.append(f"| **Ano** | **500** | **{f(500/conv)}** | **2.500** | **2.000** |")
rows2.append("| **Ano** | "+" | ".join(f"**{f(x)}**" for x in T[:6])+" |")
open("t_funil2.md","w").write("\n".join(rows)); open("t_origem2.md","w").write("\n".join(rows2))
print("\n".join(rows)); print("\n".join(rows2))
print("shares", [f(x/T[0]*100,1) for x in T[:6]])
