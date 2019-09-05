import numba.cuda.api
import numba.cuda.cudadrv.libs

numba.cuda.cudadrv.libs.test()
numba.cuda.api.detect()