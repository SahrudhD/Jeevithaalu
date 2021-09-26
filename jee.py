def MaxProfit(M,n,p,w):
  x = []
  px = []
  for i in range(n):
    x.append(0)
  c = M
  for i in range(n):
    if w[i] > c:
      break
    x[i]=1
    c = c - w[i]
  if i <= n:
    x[i] = c / w[i]   
  print(x)
  for i in range(n):
    px.append(p[i]*x[i])
  print("Optimal Solution for Maximum Profit: ", sum(px))
  return sum(px)

def MinWeight(M,n,p,w):
  x = []
  px = []
  for i in range(n):
    x.append(0)
  c = M
  for i in range(n):
    if w[n-1-i] > c:
      break
    x[n-1-i]=1
    c = c - w[n-1-i]
  if i <= n:
    x[n-1-i] = c / w[n-1-i]   
  print(x)
  for i in range(n):
    px.append(p[i]*x[i])
  print("Optimal Solution for Minimum Weight: ", sum(px))
  return sum(px)

def MaxProfitPerUnitWt(M,n,p,w):
  x = []
  px = []
  r = []
  for i in range(n):
    x.append(0)
    r.append(p[i]/w[i])
  TableSort(p,w,r,n)    
  c = 0 
  for i in range(n):
    if c + w[i] <= M:
      x[i] = 1 
      c = c + w[i] 
    else: 
      x[i] = (M - c) / w[i] 
      c = M 
      break 
  print(x)
  for i in range(n):
    px.append(p[i]*x[i])
  print("Optimal Solution for Maximum Profit per Unit Weight: ", sum(px))
  return sum(px)

def TableSort(p,w,r,n):
  for i in range(n):
    for j in range(0, n-i-1):
      if r[j] < r[j+1] :
        r[j], r[j+1] = r[j+1], r[j]
        p[j], p[j+1] = p[j+1], p[j]
        w[j], w[j+1] = w[j+1], w[j]
          
def Knapsack(M,n):
  p = []
  w = []
  for i in range(n):
    p.append(int(input("Enter Profit {}:".format(i+1))))
    w.append(int(input("Enter Weight {}:".format(i+1))))

  sol = []
  sol.append(MaxProfit(M,n,p,w))
  sol.append(MinWeight(M,n,p,w))
  sol.append(MaxProfitPerUnitWt(M,n,p,w))
  return max(sol)

M = int(input("Enter Knapsack Size: "))
n = int(input("Enter Number of Items"))
print("Maximized Solution: ", Knapsack(M,n))
    
  
  

