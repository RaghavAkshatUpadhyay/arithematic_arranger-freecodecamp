def is_int(val):
    try:
        num = int(val)
    except ValueError:
        return False
def arithmetic_arranger(problems,a=None):
  arranged_problems=""  
  c=list()
 
  if(len(problems)>5):
    return "Error: Too many problems."
    
  for i in problems:
   c.append(i.split())

  topline=""
  bottomline=""
  dashes=""
  values=""
  for i in c:
    start=i[0]
    operator=i[1]
    bottom=i[2]
    
    if operator=='*'or operator== '/':
      return "Error: Operator must be '+' or '-'."
    elif(len(start)>4 or len(bottom)>4):
      return "Error: Numbers cannot be more than four digits."
    elif(is_int(start)== False or is_int(bottom)== False):
      return "Error: Numbers must only contain digits."  
    else:
      continue


    if(operator == '+'):
      value=int(start) +int(bottom)
    else:
      value= int(start)-int(bottom)
    
    if a!=True:
      a=len(start)
      c=len(bottom)
      if(a==c):
        topline=topline+"\t"+start.rjust(a+2)
        bottomline=bottomline+"\t" + operator+bottom.rjust(a+1)
        dashes=dashes + "\t"+"-".rjust(a+2,"-")
      elif(a>c):
        topline=topline+"\t"+start.rjust(a+2)
        bottomline=bottomline+"\t"+operator+bottom.rjust(a+1)
        dashes=dashes+"\t"+"-".rjust(a+2,"-")
      else:
        topline=topline+"\t"+(start.rjust(c+2))
        bottomline=bottomline+"\t"+operator+bottom.rjust(c+1)+"-".rjust(c+2,"-")
        dashes=dashes+"\t"+"-".rjust(c+2,"-") 
    else:
      if(a==c):
        topline=topline+"\t"+start.rjust(a+2)
        bottomline=bottomline+"\t" + operator+bottom.rjust(a+1)
        dashes=dashes + "\t"+"-".rjust(a+2,"-")
        values=values+"\t"+str(value).rjust(a+2)
      elif(a>c):
        topline=topline+"\t"+start.rjust(a+2)
        bottomline=bottomline+"\t"+operator+bottom.rjust(a+1)
        dashes=dashes+"\t"+"-".rjust(a+2,"-")
        values=values+"\t"+str(value).rjust(a+2)
      else:
        topline=topline+"\t"+(start.rjust(c+2))
        bottomline=bottomline+"\t"+operator+bottom.rjust(c+1)+"-".rjust(c+2,"-")
        dashes=dashes+"\t"+"-".rjust(c+2,"-")
        values=values+"\t"+str(value).rjust(c+2)
     
  arranged_problems=topline+"\n"+bottomline+"\n"+dashes
  return arranged_problems