def opt(nums):
    #lista resultado
    res = set()
    ##Lista para los tipos de valores
    positive, negative, cero = [], [], []
    #Para los numeros en la lista de entrada Numeros
    for num in nums:
        #Si el numero es cero, se agrega en la lista cero
        if num == 0:
            cero.append(num)

        #Si numero es positivo, se agrega en la lista positive
        elif num > 0:
            positive.append(num)

        #Si numero es negative, se agrega en la lista negative
        elif num < 0 :
            negative.append(num)

    #Si la longitud de la lista es mayor a 3 (es decir, se puede formar una tupla de ceros, agregamos a res, dicha tupla)
    if len(cero) >= 3:
        res.add((0, 0, 0))

    P, N = set(positive), set(negative)

    #Si la lista cero tiene algun valor; si existe; si no es nula
    if cero:
        #Si existe un numero en positivo
        for num in P:

            #si ese mismo numero esta en los negativos
            if -num in N:

                #Agragamos la tupla -num, 0, num 
                res.add((-num, 0, num))

    #evaluamos los negativos
    for i in range(len(negative)):
        #
        for j in range(i + 1, len(negative)):

            #suma de negativos, buscamos su complemento en la lista positiva
            sumaNegativos = -(negative[i] + negative[j])
            if sumaNegativos in P:
                res.add(tuple(sorted([negative[i], negative[j], sumaNegativos])))
        
    #Evaluamos positivos
    for i in range(len(positive)):
        for j in range(i + 1, len(positive)):

            #suma de positivos y buscamos el complemento en los negativos
            sumaPositivos = -(positive[i] + positive[j])
            if sumaPositivos in N:
                res.add(tuple(sorted([positive[i], positive[j], sumaPositivos])))
         
    return res

        

