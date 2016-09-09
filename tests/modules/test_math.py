from ..utils import ModuleFunctionTestCase, TranspileTestCase

class MathTests(ModuleFunctionTestCase, TranspileTestCase):
    ModuleFunctionTestCase.add_one_arg_tests('math', [
        'acos',
        'acosh',
        'asin',
        'asinh',
        'atan',
        'atanh',
        'ceil',
        'cos',
        'cosh',
        'degrees',
        'exp',
        'expm1',
        'erf',
        'erfc',
        'fabs',
        'factorial',
        'floor',
        'frexp',
        'log',
        'log10',
        'log1p',
        'log2',
        'radians',
        'sin',
        'sinh',
        'sqrt',
        'tan',
        'tanh',
    ])

    ModuleFunctionTestCase.add_two_arg_tests('math', [
        # 'atan2', # commented out because they take too long in CircleCI
        # 'copysign',
        # 'fmod',
        # 'log',
        # 'pow',
    ])

    TODO = [
        'fsum',
        'gamma',
        'gcd',
        'hypot',
        'isclose',
        'isfinite',
        'isinf',
        'isnan',
        'ldexp',
        'lgamma',
        'modf',
        'trunc',
    ]


    not_implemented = [
        'test_math_acos_float',
        'test_math_acos_frozenset',
        'test_math_acos_int',

        'test_math_acosh_float',
        'test_math_acosh_frozenset',

        'test_math_asin_float',
        'test_math_asin_frozenset',
        'test_math_asin_int',

        'test_math_asinh_float',
        'test_math_asinh_frozenset',
        'test_math_asinh_int',

        'test_math_atan2_bool_frozenset',
        'test_math_atan2_bytearray_frozenset',
        'test_math_atan2_bytes_frozenset',
        'test_math_atan2_class_frozenset',
        'test_math_atan2_complex_frozenset',
        'test_math_atan2_dict_frozenset',
        'test_math_atan2_float_frozenset',
        'test_math_atan2_frozenset_bool',
        'test_math_atan2_frozenset_bytearray',
        'test_math_atan2_frozenset_bytes',
        'test_math_atan2_frozenset_class',
        'test_math_atan2_frozenset_complex',
        'test_math_atan2_frozenset_dict',
        'test_math_atan2_frozenset_float',
        'test_math_atan2_frozenset_frozenset',
        'test_math_atan2_frozenset_int',
        'test_math_atan2_frozenset_list',
        'test_math_atan2_frozenset_None',
        'test_math_atan2_frozenset_NotImplemented',
        'test_math_atan2_frozenset_range',
        'test_math_atan2_frozenset_set',
        'test_math_atan2_frozenset_slice',
        'test_math_atan2_frozenset_str',
        'test_math_atan2_frozenset_tuple',
        'test_math_atan2_int_frozenset',
        'test_math_atan2_int_int',
        'test_math_atan2_list_frozenset',
        'test_math_atan2_None_frozenset',
        'test_math_atan2_NotImplemented_frozenset',
        'test_math_atan2_range_frozenset',
        'test_math_atan2_set_frozenset',
        'test_math_atan2_slice_frozenset',
        'test_math_atan2_str_frozenset',
        'test_math_atan2_tuple_frozenset',

        'test_math_atan_frozenset',

        'test_math_atanh_frozenset',

        'test_math_ceil_frozenset',

        'test_math_copysign_bool_frozenset',
        'test_math_copysign_bytearray_frozenset',
        'test_math_copysign_bytes_frozenset',
        'test_math_copysign_class_frozenset',
        'test_math_copysign_complex_frozenset',
        'test_math_copysign_dict_frozenset',
        'test_math_copysign_float_frozenset',
        'test_math_copysign_frozenset_bool',
        'test_math_copysign_frozenset_bytearray',
        'test_math_copysign_frozenset_bytes',
        'test_math_copysign_frozenset_class',
        'test_math_copysign_frozenset_complex',
        'test_math_copysign_frozenset_dict',
        'test_math_copysign_frozenset_float',
        'test_math_copysign_frozenset_frozenset',
        'test_math_copysign_frozenset_int',
        'test_math_copysign_frozenset_list',
        'test_math_copysign_frozenset_None',
        'test_math_copysign_frozenset_NotImplemented',
        'test_math_copysign_frozenset_range',
        'test_math_copysign_frozenset_set',
        'test_math_copysign_frozenset_slice',
        'test_math_copysign_frozenset_str',
        'test_math_copysign_frozenset_tuple',
        'test_math_copysign_int_frozenset',
        'test_math_copysign_list_frozenset',
        'test_math_copysign_None_frozenset',
        'test_math_copysign_NotImplemented_frozenset',
        'test_math_copysign_range_frozenset',
        'test_math_copysign_set_frozenset',
        'test_math_copysign_slice_frozenset',
        'test_math_copysign_str_frozenset',
        'test_math_copysign_tuple_frozenset',

        'test_math_cos_frozenset',

        'test_math_cosh_frozenset',

        'test_math_degrees_frozenset',

        'test_math_erf_frozenset',

        'test_math_erfc_frozenset',

        'test_math_exp_frozenset',

        'test_math_expm1_frozenset',

        'test_math_fabs_frozenset',

        'test_math_factorial_frozenset',

        'test_math_floor_frozenset',

        'test_math_fmod_bool_frozenset',
        'test_math_fmod_bytearray_frozenset',
        'test_math_fmod_bytes_frozenset',
        'test_math_fmod_class_frozenset',
        'test_math_fmod_complex_frozenset',
        'test_math_fmod_dict_frozenset',
        'test_math_fmod_float_frozenset',
        'test_math_fmod_frozenset',
        'test_math_fmod_frozenset_bool',
        'test_math_fmod_frozenset_bytearray',
        'test_math_fmod_frozenset_bytes',
        'test_math_fmod_frozenset_class',
        'test_math_fmod_frozenset_complex',
        'test_math_fmod_frozenset_dict',
        'test_math_fmod_frozenset_float',
        'test_math_fmod_frozenset_frozenset',
        'test_math_fmod_frozenset_int',
        'test_math_fmod_frozenset_list',
        'test_math_fmod_frozenset_None',
        'test_math_fmod_frozenset_NotImplemented',
        'test_math_fmod_frozenset_range',
        'test_math_fmod_frozenset_set',
        'test_math_fmod_frozenset_slice',
        'test_math_fmod_frozenset_str',
        'test_math_fmod_frozenset_tuple',
        'test_math_fmod_int_frozenset',
        'test_math_fmod_list_frozenset',
        'test_math_fmod_None_frozenset',
        'test_math_fmod_NotImplemented_frozenset',
        'test_math_fmod_range_frozenset',
        'test_math_fmod_set_frozenset',
        'test_math_fmod_slice_frozenset',
        'test_math_fmod_str_frozenset',
        'test_math_fmod_tuple_frozenset',

        'test_math_frexp_frozenset',

        'test_math_log_bool_frozenset',
        'test_math_log_bytearray_frozenset',
        'test_math_log_bytes_frozenset',
        'test_math_log_class_frozenset',
        'test_math_log_complex_frozenset',
        'test_math_log_dict_frozenset',
        'test_math_log_float_frozenset',
        'test_math_log_float_int',
        'test_math_log_frozenset',
        'test_math_log_frozenset_bool',
        'test_math_log_frozenset_bytearray',
        'test_math_log_frozenset_bytes',
        'test_math_log_frozenset_class',
        'test_math_log_frozenset_complex',
        'test_math_log_frozenset_dict',
        'test_math_log_frozenset_float',
        'test_math_log_frozenset_frozenset',
        'test_math_log_frozenset_int',
        'test_math_log_frozenset_list',
        'test_math_log_frozenset_None',
        'test_math_log_frozenset_NotImplemented',
        'test_math_log_frozenset_range',
        'test_math_log_frozenset_set',
        'test_math_log_frozenset_slice',
        'test_math_log_frozenset_str',
        'test_math_log_frozenset_tuple',
        'test_math_log_int',
        'test_math_log_int_float',
        'test_math_log_int_int',
        'test_math_log_int_frozenset',
        'test_math_log_list_frozenset',
        'test_math_log_None_frozenset',
        'test_math_log_NotImplemented_frozenset',
        'test_math_log_range_frozenset',
        'test_math_log_set_frozenset',
        'test_math_log_slice_frozenset',
        'test_math_log_str_frozenset',
        'test_math_log_tuple_frozenset',

        'test_math_log10_bool',
        'test_math_log10_float',
        'test_math_log10_frozenset',
        'test_math_log10_int',

        'test_math_log1p_float',
        'test_math_log1p_frozenset',
        'test_math_log1p_int',

        'test_math_log2_float',
        'test_math_log2_frozenset',
        'test_math_log2_int',

        'test_math_pow_bool_frozenset',
        'test_math_pow_bytearray_frozenset',
        'test_math_pow_bytes_frozenset',
        'test_math_pow_class_frozenset',
        'test_math_pow_complex_frozenset',
        'test_math_pow_dict_frozenset',
        'test_math_pow_float_frozenset',
        'test_math_pow_frozenset_bool',
        'test_math_pow_frozenset_bytearray',
        'test_math_pow_frozenset_bytes',
        'test_math_pow_frozenset_class',
        'test_math_pow_frozenset_complex',
        'test_math_pow_frozenset_dict',
        'test_math_pow_frozenset_float',
        'test_math_pow_frozenset_frozenset',
        'test_math_pow_frozenset_int',
        'test_math_pow_frozenset_list',
        'test_math_pow_frozenset_None',
        'test_math_pow_frozenset_NotImplemented',
        'test_math_pow_frozenset_range',
        'test_math_pow_frozenset_set',
        'test_math_pow_frozenset_slice',
        'test_math_pow_frozenset_str',
        'test_math_pow_frozenset_tuple',
        'test_math_pow_int_frozenset',
        'test_math_pow_list_frozenset',
        'test_math_pow_None_frozenset',
        'test_math_pow_NotImplemented_frozenset',
        'test_math_pow_range_frozenset',
        'test_math_pow_set_frozenset',
        'test_math_pow_slice_frozenset',
        'test_math_pow_str_frozenset',
        'test_math_pow_tuple_frozenset',

        'test_math_radians_frozenset',

        'test_math_sin_frozenset',

        'test_math_sinh_frozenset',

        'test_math_sqrt_frozenset',

        'test_math_tan_frozenset',

        'test_math_tanh_frozenset',
    ]

    def test_constants(self):
        self.assertCodeExecution("""
            import math
            print(math.e)
            print(math.inf)
            print(math.nan)
            print(math.pi)
            """)

    def test_erf(self):
        # test some of the edge cases of erf to 15 digits of precision
        self.assertCodeExecution("""
            import math
            print(round(math.erf(0.75) * (10**15)))
            print(round(math.erf(1.40) * (10**15)))
            print(round(math.erf(1.60) * (10**15)))
            """)

    def test_frexp(self):
        # test some of the edge cases of for frexp
        self.assertCodeExecution("""
            import math
            print(math.frexp(float('nan')))
            print(math.frexp(float('inf')))
            print(math.frexp(float('-inf')))
            print(math.frexp(-0.0))
            print(math.frexp(0.0))
            print(math.frexp(2**-1026)) # denormal
            print(math.frexp(2**-1027)) # denormal
            print(math.frexp(1.9**-1150)) # denormal
            """)


    def test_docstrings(self):
        self.assertCodeExecution("""
        import math
        print(math.acos.__doc__)
        print(math.acosh.__doc__)
        print(math.asin.__doc__)
        print(math.asinh.__doc__)
        print(math.atan.__doc__)
        print(math.atan2.__doc__)
        print(math.atanh.__doc__)
        print(math.ceil.__doc__)
        print(math.copysign.__doc__)
        print(math.cos.__doc__)
        print(math.cosh.__doc__)
        print(math.degrees.__doc__)
        print(math.erf.__doc__)
        print(math.erfc.__doc__)
        print(math.exp.__doc__)
        print(math.expm1.__doc__)
        print(math.fabs.__doc__)
        print(math.factorial.__doc__)
        print(math.floor.__doc__)
        print(math.fmod.__doc__)
        print(math.frexp.__doc__)
        print(math.fsum.__doc__)
        print(math.gamma.__doc__)
        print(math.gcd.__doc__)
        print(math.hypot.__doc__)
        print(math.isclose.__doc__)
        print(math.isfinite.__doc__)
        print(math.isinf.__doc__)
        print(math.isnan.__doc__)
        print(math.ldexp.__doc__)
        print(math.lgamma.__doc__)
        print(math.log.__doc__)
        print(math.log10.__doc__)
        print(math.log1p.__doc__)
        print(math.log2.__doc__)
        print(math.modf.__doc__)
        print(math.pow.__doc__)
        print(math.radians.__doc__)
        print(math.sin.__doc__)
        print(math.sinh.__doc__)
        print(math.sqrt.__doc__)
        print(math.tan.__doc__)
        print(math.tanh.__doc__)
        print(math.trunc.__doc__)
        """)