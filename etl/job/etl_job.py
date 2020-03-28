from time import time
from etl.job.config import ETLConfig as cfg
from etl.extractor.azair_content_parser import AZAirContentParser
from etl.transformer.azair_content_transformer import AZAirContentTransformer
from etl.loader.azair_content_loader import AZAirContentLoader


class ETLJob:

    def __init__(self, extractor, transformer, loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run(self):
        try:
            self._execute_pipeline()
            return "SUCCESS"
        except Exception as err:
            print(err)
            return "FAILED"

    def _execute_pipeline(self):
        #EXTRACT
        raw_content = self.extractor.extract_content()
        #TRANSFORM
        content = self.transformer.transform_raw_content(
            raw_content=raw_content
        )
        #LOAD
        self.loader.load_content(
            content=content
        )


def time_func(function):

    def wrapper(*args, **kwargs):

        execution_start = time()
        result = function(*args, **kwargs)
        execution_end = time()

        execution_time = (execution_end - execution_start)
        print(f"Execution time: {execution_time:.2f} s")

        return result
    
    return wrapper


@time_func
def run_etl_job():

    extractor = AZAirContentParser(cfg.URL, cfg.PARAMS)
    transformer = AZAirContentTransformer(cfg.PARSER)
    loader = AZAirContentLoader(cfg.CHUNK_SIZE)
    
    etl = ETLJob(
        extractor=extractor,
        transformer=transformer,
        loader=loader
    )

    status = etl.run()
    print(f"Job status: {status}")
