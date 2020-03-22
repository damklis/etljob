from etl.config import ETLConfig as cfg
from etl.extractor.azair_content_parser import AZAirContentParser
from etl.transformer.azair_content_transformer import AZAirContentTransformer


class ETLJob:

    def __init__(self, extractor, transformer, loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run(self):
        raw_content = self.extractor.extract_content()
        content = self.transformer.transform_raw_content(
            raw_content=raw_content
        )

        for i in content:
            print(i)
        #self.loader.load_data(transformed_data)



def run_etl_job():
    extractor = AZAirContentParser(cfg.URL, cfg.PARAMS)
    transformer = AZAirContentTransformer(cfg.PARSER)
    loader = None
    
    etl = ETLJob(
        extractor=extractor,
        transformer=transformer,
        loader=loader
    )

    etl.run()