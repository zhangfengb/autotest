"""二叉树的层序遍历"""

hou,mid = input().split()

def dfs(hou,mid,res,queue):

    root = hou[-1]
    res.append(root)

    index = mid.find(root)
    if index > 0:
        queue.append([hou[:index],mid[:index]])
    if len(mid) - index - 1 >0:
        queue.append([hou[index:-1],mid[index+1:]])

    return res
def getResult(hou,mid):
    res = []
    queue = []
    dfs(hou,mid,res,queue)

    while len(queue)>0:
        hou1,zhong1 = queue.pop(0)
        dfs(hou1,zhong1,res,queue)
    return ''.join(res)
print(getResult(hou,mid))