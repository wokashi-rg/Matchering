from matchering import DSPModule
from matchering import pcm16, pcm24, Result

module = DSPModule(log=print, show_codes=True)
module.process(
    target='my_mix.wav',
    reference='reference.flac',
    results=[
        pcm24('result_24bit.wav'),
        pcm16('result_16bit.wav'),

        Result(
            'custom_result_24bit_no_limiter.flac',
            'PCM_24',
            use_limiter=False
        ),
        Result(
            'custom_result_32bit_no_limiter_non-normalized.aiff',
            'FLOAT',
            use_limiter=False,
            normalize=False
        ),
    ]
)