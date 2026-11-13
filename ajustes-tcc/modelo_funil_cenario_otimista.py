M=["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
A=[26,40,64,60,68,74,86,92,100,109,139,126]
B=[18,26,43,51,62,69,74,82,86,92,120,113]
R=[7336.76,11049.34,17728.33,18165.10,21277.10,23395.97,26261.00,28569.66,30542.94,33129.79,42497.01,39208.21]
P=[a+b for a,b in zip(A,B)]
def f(x,d=0): return f"{x:,.{d}f}".replace(",","X").replace(".",",").replace("X",".")
# new clients proportional to orders, sum 500 (largest remainder)
n=[44,52,71,52,52,52,52,52,52,59,78,34]


print("new",n,sum(n))
rec=[p-x for p,x in zip(P,n)]
print("recurr",rec,sum(rec), sum(rec)/sum(P))
# metas table
rows=["| Mês | Caixas avulsas | Caixas de assinatura | Total de pedidos | Receita avulsa (R$) | Receita de assinatura (R$) | Receita total (R$) |","| --- | --- | --- | --- | --- | --- | --- |"]
for m in range(12):
    rows.append(f"| {M[m]}/27 | {A[m]} | {B[m]} | {P[m]} | {f(A[m]*179.99,2)} | {f(B[m]*145.99,2)} | {f(R[m],2)} |")
rows.append(f"| **Ano** | **{sum(A)}** | **{sum(B)}** | **{sum(P)}** | **{f(sum(A)*179.99,2)}** | **{f(sum(B)*145.99,2)}** | **{f(sum(R),2)}** |")
open("t4_metas.md","w").write("\n".join(rows)); print("\n".join(rows))
# funnel
conv=0.0109
ads=[3528,2117,4234,2470,2470,2470,2470,2822,2822,3175,4586,2116]
seo=[30,50,80,120,170,230,300,380,460,540,620,700]
r1=["| Mês | Novas clientes | Visitas necessárias | Carrinhos criados | Carrinhos abandonados |","| --- | --- | --- | --- | --- |"]
r2=["| Mês | Total de visitas | Anúncios pagos | Influência e parcerias | Redes orgânicas | Busca (SEO) | Direto, e-mail e lista |","| --- | --- | --- | --- | --- | --- | --- |"]
T=[0]*6
for m in range(12):
    v=n[m]/conv; c=n[m]/.2; p=ads[m]/2; d=v*.05; s=seo[m]; rest=v-p-d-s
    r1.append(f"| {M[m]}/27 | {n[m]} | {f(v)} | {f(c)} | {f(c-n[m])} |")
    r2.append(f"| {M[m]}/27 | {f(v)} | {f(p)} | {f(rest/2)} | {f(rest/2)} | {f(s)} | {f(d)} |")
    for k,x in enumerate([v,p,rest/2,rest/2,s,d]): T[k]+=x
r1.append(f"| **Ano** | **650** | **{f(650/conv)}** | **3.250** | **2.600** |")
r2.append("| **Ano** | "+" | ".join(f"**{f(x)}**" for x in T)+" |")
open("t4_funil.md","w").write("\n".join(r1)); open("t4_origem.md","w").write("\n".join(r2))
print("\n".join(r1)); print("\n".join(r2)); print([round(x/T[0]*100,1) for x in T])
# recurring table
r3=["| Mês | Pedidos de novas clientes | Pedidos recorrentes | % recorrentes |","| --- | --- | --- | --- |"]
for m in range(12): r3.append(f"| {M[m]}/27 | {n[m]} | {rec[m]} | {f(rec[m]/P[m]*100)}% |")
r3.append(f"| **Ano** | **650** | **{sum(rec)}** | **{f(sum(rec)/sum(P)*100)}%** |")
open("t4_rec.md","w").write("\n".join(r3)); print("\n".join(r3))
# contribution
ca,cs=93.46,62.40
contrib=sum(A)*ca+sum(B)*cs
print("contrib",contrib, contrib-126400, contrib/650, contrib/650/252.8, "meses CAC", 252.8/cs)
# demand/stock
mk=[9,9,22,22,22,22,22,22,22,22,26,22]; ev=[8]+[0]*11
lots=[0]*12; st=600; out=[]
r4=["| Mês | Caixas vendidas | Contatos de atendimento | Horas de atendimento | Uso da capacidade | Caixas para marketing e amostras | Lote recebido | Estoque no fim do mês |","| --- | --- | --- | --- | --- | --- | --- | --- |"]
L={}
for m in range(12):
    d=P[m]+mk[m]+ev[m]
    nxt=(P[m+1]+mk[m+1]) if m<11 else 200
    if st-d < nxt: L[m]=500; st+=500
    st-=d
    ct=P[m]*.3; h=ct*.1
    r4.append(f"| {M[m]}/27 | {P[m]} | {f(ct)} | {f(h,1)} | {f(h/43.3*100)}% | {mk[m]+ev[m]} | {L.get(m,'–')} | {st} |")
tot=sum(P)+sum(mk)+8
r4.append(f"| **Ano** | **{f(sum(P))}** | **{f(sum(P)*.3)}** | **{f(sum(P)*.03,1)}** | **máx. {f(max(P)*.03/43.3*100)}%** | **{sum(mk)+8}** | **{f(sum(L.values()))}** | **{st}** |")
open("t4_dem.md","w").write("\n".join(r4)); print("\n".join(r4)); print("demand",tot,L)
