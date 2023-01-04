from core import *


def func(i,W1,contDat,W3,W2,T_3):
    openerD = np.array(np.array([[1, 2, 4], [2, 4, 8], [4, 8, 16]])[i])
    referdat = refer[i]
    s1 = Hid(fullOper(openerD, W1), fullOper(contDat, W3), T_2)
    res = siggmThan(fullOper(siggmThan(s1), W2) - T_3)
    contDat = np.array(res)
    W2 = W2 - alpha * (res - referdat) * np.array([siggmThan(s1)]).transpose()
    T_3 = T_3 + alpha * (res[0] - referdat)
    gamma_matrix = (res - referdat) * W2
    a = [gamma_matrix, res , referdat, s1, openerD, W2, T_3]
    return a

def run(alpha, refer, contDat, T_2, T_3, e,frthCount , secondC, resUlt, E):
    context_layer_count = resUlt
    W1 = randomWeight(frthCount, secondC)
    W2 = randomWeight(secondC, resUlt)
    W3 = randomWeight(context_layer_count, secondC)
    while True:
        E = 0
        len_range = len(np.array([[1, 2, 4], [2, 4, 8], [4, 8, 16]]))
        for i in range(len_range):
            params = func(i, W1, contDat, W3, W2, T_3)
            gamma_matrix, res , referdat, s1, openerD, W2, T_3 = params[0], params[1], params[2], params[3],params[4], params[5],params[6]
            E_par = res[0] - referdat
            E_i = E_par ** 2
            E += E_i
            print("RESULT = ", res,
                  "; REQUiREMENTOS = ",
                  refer[i])
        print('')
        print('Errrrror: ', E)
        print('')
        if E <= e: # ERRRRRRRRROR
            break

    progn(W1, contDat, W3, T_2, W2, T_3, 1)


if __name__ == '__main__':
    alpha = 0.01
    refer = [8, 16, 32]
    cont = [0]
    T_2 = np.array([[0, 0]])
    T_3 = 0
    e = 0.000000000000000001
    frthCount = 3
    secondC = 2
    resUlt = 1
    run(alpha, refer, cont, T_2, T_3, e,frthCount , secondC, resUlt, 0)\


