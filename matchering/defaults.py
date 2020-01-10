import math


class LimiterConfig:
    def __init__(
            self,
            attack: float = 1,
            hold: float = 1,
            release: float = 3000,
            attack_filter_coefficient: float = -2,
            hold_filter_order: int = 1,
            hold_filter_coefficient: float = 7,
            release_filter_order: int = 1,
            release_filter_coefficient: float = 800
    ):
        assert attack > 0
        self.attack = attack

        assert hold > 0
        self.hold = hold

        assert release > 0
        self.release = release

        self.attack_filter_coefficient = attack_filter_coefficient

        assert hold_filter_order > 0
        assert isinstance(hold_filter_order, int)
        self.hold_filter_order = hold_filter_order

        self.hold_filter_coefficient = hold_filter_coefficient

        assert release_filter_order > 0
        assert isinstance(release_filter_order, int)
        self.release_filter_order = release_filter_order

        self.release_filter_coefficient = release_filter_coefficient


class MainConfig:
    def __init__(
            self,
            internal_sample_rate: int = 44100,
            max_length: float = 15 * 60,
            max_piece_size: float = 15,
            threshold: float = (2 ** 15 - 61) / 2 ** 15,
            min_value: float = 1e-6,
            fft_size: int = 4096,
            lin_log_oversampling: int = 4,
            rms_correction_steps: int = 4,
            clipping_samples_threshold: int = 8,
            limited_samples_threshold: int = 128,
            lowess_frac: float = 0.0375,
            lowess_it: int = 0,
            lowess_delta: float = 0.001,
            preview_size: float = 30,
            preview_analysis_step: float = 5,
            preview_fade_size: float = 1,
            preview_fade_coefficient: float = 8,
            temp_folder: str = None,
            limiter: LimiterConfig = LimiterConfig(),
    ):
        assert internal_sample_rate > 0
        assert isinstance(internal_sample_rate, int)
        self.internal_sample_rate = internal_sample_rate

        assert max_length > 0
        assert max_length > fft_size / internal_sample_rate
        self.max_length = max_length

        assert threshold > min_value
        assert threshold < 1
        self.threshold = threshold

        assert min_value > 0
        assert min_value < 0.1
        self.min_value = min_value

        assert max_piece_size > 0
        assert max_piece_size > fft_size / internal_sample_rate
        assert max_piece_size < max_length
        self.max_piece_size = max_piece_size * internal_sample_rate

        assert fft_size > 1
        assert math.log2(fft_size).is_integer()
        self.fft_size = fft_size

        assert lin_log_oversampling > 0
        assert isinstance(lin_log_oversampling, int)
        self.lin_log_oversampling = lin_log_oversampling

        assert rms_correction_steps >= 0
        assert isinstance(rms_correction_steps, int)
        self.rms_correction_steps = rms_correction_steps

        assert clipping_samples_threshold >= 0
        assert limited_samples_threshold > 0
        assert limited_samples_threshold > clipping_samples_threshold
        assert isinstance(clipping_samples_threshold, int)
        assert isinstance(limited_samples_threshold, int)
        self.clipping_samples_threshold = clipping_samples_threshold
        self.limited_samples_threshold = limited_samples_threshold

        assert lowess_frac > 0
        assert lowess_it >= 0
        assert lowess_delta >= 0
        assert isinstance(lowess_it, int)
        self.lowess_frac = lowess_frac
        self.lowess_it = lowess_it
        self.lowess_delta = lowess_delta

        assert preview_size > 5
        assert preview_analysis_step > 1
        assert preview_fade_size > 0
        assert preview_fade_coefficient >= 2
        self.preview_size = preview_size * internal_sample_rate
        self.preview_analysis_step = preview_analysis_step * internal_sample_rate
        self.preview_fade_size = preview_fade_size * internal_sample_rate
        self.preview_fade_coefficient = preview_fade_coefficient

        assert temp_folder is None or isinstance(temp_folder, str)
        self.temp_folder = temp_folder

        assert isinstance(limiter, LimiterConfig)
        self.limiter = limiter
