# Classes and methods whitelist
core = {'': ['absdiff', 'add', 'addWeighted', 'bitwise_and', 'bitwise_not', 'bitwise_or', 'bitwise_xor', 'cartToPolar',\
             'compare', 'convertScaleAbs', 'countNonZero', 'determinant', 'dft', 'divide', 'eigen', \
             'exp', 'flip', 'gemm', 'hconcat', 'inRange', 'invert', 'kmeans', 'log', 'magnitude', \
             'max', 'mean', 'meanStdDev', 'merge', 'min', 'minMaxLoc', 'mixChannels', 'multiply', 'norm', 'normalize', \
             'perspectiveTransform', 'polarToCart', 'pow', 'randn', 'randu', 'reduce', 'repeat', 'setIdentity', 'setRNGSeed', \
             'solve', 'solvePoly', 'split', 'sqrt', 'subtract', 'trace', 'transform', 'transpose', 'vconcat'],
        'Algorithm': []}

imgproc = {'': [ 'resize'],}

white_list = makeWhiteList([core, imgproc])
