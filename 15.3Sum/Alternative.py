#MENOS EFICIENTE
def fun(nums):

    #Iniciamos lista
    result = []
    i = 0

    
    while i < len(nums):
        j = i + 1
        while j != i:

            #Si j se pasa de limite de index vuelve a cero
            if j == len(nums):
                j = 0
            
            k = j + 1

            #Buscamos el limite para iteracion de k, buscando el limite mas cercano a len entre i y j
            mayor = 0
            if(i > j):
                mayor = i
            else:
                mayor = j
            while k != mayor:

                #Si k se pasa de limite de index vuelve a cero
                if k == len(nums):
                    k = 0

                #Condicion del ejercicio
                if(k != i and k != j and (nums[i] + nums[j] + nums[k]) == 0):

                    #Creamos la tupla y la ordenamos
                    triplet = []
                    triplet.append(nums[i])
                    triplet.append(nums[j])
                    triplet.append(nums[k])
                    triplet.sort()
                        
                    #Si la tupla no esta en result, la agrega
                    #NO ES UNA FORMA EFICIENTE DE HACER EL EJERCICIO POR QUE 
                    #ITERA INECESARIAMENTE
                    if triplet not in result:
                        result.append(triplet)
                    
                k = k + 1
            j = j + 1
        i = i + 1
    return result
                
