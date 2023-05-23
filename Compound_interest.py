def com(p,r,t):
    am=p*(pow((1+r/100),t))
    ci=am
    print("%.2f"%(ci))
p,r,t=map(int,input().split())
com(p,r,t)