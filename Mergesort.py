#Python program for implementation of MergeSort(Recersive):

def merge_sort(mylst):
     if len(mylst)>1:
          mid = len(mylst)//2
          left = mylst[:mid]
          right = mylst[mid:]

          merge_sort(left)
          merge_sort(right)

          i = 0

          j = 0

          k = 0

          while i<len(left) and j<len(right):
               if left[i]<right[j]:
                    mylst[k] = left[i]

                    i+=1
               else:
                    mylst[k] = right[j]

                    j+=1
               k+=1

          while i < len(left):
               mylst[k] = left[i]
               i+=1
               k+=1
          while j <len(right):
               mylst[k] = right[j]
               j+=1
               k+=1
                    
mylst =[50,25,22,17,18,4,13,19,20,3,12]
merge_sort(mylst)
print(mylst)
