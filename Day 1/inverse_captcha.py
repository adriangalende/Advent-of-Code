# --- Dia 1: Inverse Captcha - --
# Parte 1
# El captcha requiere que revises una secuencia de digitos (la entrada de tu puzzle)
# y encuentres la suma de todos los digitos que coincidan con el siguiente digito de la lista.
# La lista es circular, asi que el digito de despues del ultimo es el primer digito de la lista.
#
# Por ejemplo:
#
# 1122 produce la suma de 3 (1 + 2) porque el primer digito (1)  coincide con el segundo digito
# y el tercer digito (2) coincide con el cuarto.
# 1111 produce 4 porque cada digito (todos 1) coinciden con el siguiente.
# 1234 produce 0 porque ninguno de los digito coincide con el siguiente.
# 91212129 produce 9 porque el unico digito que coincide con el siguiente es el ultimo (9).
#
#¿Cual es la solucion al captcha?

def resolverCaptcha(numero):
    sumaNumeros = 0
    for indice in range(len(numero)):
        """
            #(index+1)%len(numero) devuelve el resto de dividir el (índice / longitud de nuestro String)
            así podemos realizar la comparación de la lista de forma circular:
                cuando index+1 == longitud String cogerá el primer índice (0)
        """
        if numero[indice] == numero[(indice+1)%len(numero)]:
            sumaNumeros += int(numero[indice])
    return sumaNumeros

# Parte 2
# Te habrás dado cuenta de que la barra de progreso se ha puesto al 50%. Aparentemente, todavía no has resuelto el enigma por completo, pero te hemos dado una estrella como estímulo
# las instrucciones han cambiado:
# Ahora, en lugar de considerar el próximo dígito, tienes que tener en cuenta el número que está en la mitad de la lista.
# por suerte tu lista tiene un número par de elementos
#
#Por ejemplo:
#
#1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
#1221 produces 0, because every comparison is between a 1 and a 2.
#123425 produces 4, because both 2s match each other, but no other digit has a match.
#123123 produces 12.
#12131415 produces 4.


def resolverCaptcha2Parte(numero):
    sumaNumeros = 0
    #la cantidad de "saltos" que tenemos que realizar para comparar los números
    # dividimos entre 2 porque sabemos que todos las longitudes de listas de digitos serán par
    saltosHastaMitad = int(len(numero)/2)
    for indice in range(len(numero)):
        if numero[indice] == numero[(indice+saltosHastaMitad)%len(numero)]:
            sumaNumeros += int(numero[indice])
    return sumaNumeros


if __name__ == "__main__":
    #casos test basicos primera parte
    basicTestCase = [("1122",3),("1111",4),("1234",0),("91212129",9)]
    #Caso test a solucionar primera parte
    testCase = "428122498997587283996116951397957933569136949848379417125362532269869461185743113733992331379856446362482129646556286611543756564275715359874924898113424472782974789464348626278532936228881786273586278886575828239366794429223317476722337424399239986153675275924113322561873814364451339186918813451685263192891627186769818128715595715444565444581514677521874935942913547121751851631373316122491471564697731298951989511917272684335463436218283261962158671266625299188764589814518793576375629163896349665312991285776595142146261792244475721782941364787968924537841698538288459355159783985638187254653851864874544584878999193242641611859756728634623853475638478923744471563845635468173824196684361934269459459124269196811512927442662761563824323621758785866391424778683599179447845595931928589255935953295111937431266815352781399967295389339626178664148415561175386725992469782888757942558362117938629369129439717427474416851628121191639355646394276451847131182652486561415942815818785884559193483878139351841633366398788657844396925423217662517356486193821341454889283266691224778723833397914224396722559593959125317175899594685524852419495793389481831354787287452367145661829287518771631939314683137722493531318181315216342994141683484111969476952946378314883421677952397588613562958741328987734565492378977396431481215983656814486518865642645612413945129485464979535991675776338786758997128124651311153182816188924935186361813797251997643992686294724699281969473142721116432968216434977684138184481963845141486793996476793954226225885432422654394439882842163295458549755137247614338991879966665925466545111899714943716571113326479432925939227996799951279485722836754457737668191845914566732285928453781818792236447816127492445993945894435692799839217467253986218213131249786833333936332257795191937942688668182629489191693154184177398186462481316834678733713614889439352976144726162214648922159719979143735815478633912633185334529484779322818611438194522292278787653763328944421516569181178517915745625295158611636365253948455727653672922299582352766484"
    #Resolviendo casos test primera parte
    print(" casos test primera parte")
    for casoTest,resultado in basicTestCase:
        assert resolverCaptcha(casoTest) == resultado, "error casotest : " + casoTest
        print("caso test: " + casoTest + " pasado")

    #print(resolverCaptcha(testCase))

    #casos test basicos segunda parte
    basicTestCase = [("1212",6),("1221",0),("123425",4),("123123",12),("12131415",4)]
    #Resolviendo casos test segunda parte
    print(" casos test segunda parte")
    for casoTest,resultado in basicTestCase:
        assert resolverCaptcha2Parte(casoTest) == resultado, "error casotest : " + casoTest
        print("caso test: " + casoTest + " pasado")

    #print(resolverCaptcha2Parte(testCase))
