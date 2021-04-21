import pandas as pd
from ds_discovery import *

__author__ = 'Darryl Oatridge'


class MemberFactory(object):

    def __init__(self, uri_pm_repo: str=None, has_contract: bool=None, default_save: bool=None):
        has_contract = has_contract if isinstance(has_contract, bool) else True
        self.builder = SyntheticBuilder.from_env('members', uri_pm_repo=uri_pm_repo, has_contract=has_contract,
                                                 default_save=default_save)
        self.tr = Transition.from_env('members', uri_pm_repo=uri_pm_repo, has_contract=has_contract,
                                      default_save=default_save)

    def data_builder(self, sample_size: int):
        tools = self.builder.tools
        self.builder.pm.reset_intents()
        self.builder.pm_persist()
        df = pd.DataFrame(index=range(sample_size))
        # member_id
        df['member_id'] = tools.get_number(from_value=123456789, to_value=999999937, at_most=1, size=sample_size,
                                           column_name='member_id')
        self.builder.add_column_description(column_name='member_id', description="a unique id for the member")
        df = tools.model_sample_map(canonical=df, sample_map='us_persona', female_bias=0.55, column_name='persona')
        self.builder.add_column_description(column_name='persona', description="a base person template")
        state_code = ['CA', 'NY', 'LA', 'NJ', 'VA', 'CO', 'NV', 'GA', 'IN', 'OH', 'KY', 'ME', 'MO', 'WI']
        df = tools.model_sample_map(canonical=df, sample_map='us_zipcode', state_filter=state_code,
                                    column_name='zipcodes')
        self.builder.add_column_description(column_name='zipcodes', description="Only covering 14 states with a "
                                                                                "distribution based on population "
                                                                                "density")
        return df


if __name__ == '__main__':
    factory = MemberFactory(has_contract=False)
    result = factory.data_builder(sample_size=10)
    print(result)
