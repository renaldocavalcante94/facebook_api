from .api_base import APIBase
import pandas as pd

class FacebookAdsAPI(APIBase):

    def __init__(self,ad_account_id,access_token):
        
        self.ad_account_id = ad_account_id
        self.base_url = "https://graph.facebook.com/v10.0/"
        self.access_token = access_token
        self.access_token_uri = f"access_token={access_token}"
        super().__init__()
        
    def get_ad_account(self):
        uri = self.base_url + f"{self.ad_account_id}/" + "?"
        params = {"access_token": self.access_token}
        result = self.make_get(uri,params,return_type='json')
    
        return result

    def get_all_campaings(self,as_df=False):
            node_name = "campaigns"
            fields = """id,account_id,budget_remaining,buying_type,configured_status,created_time,
                        daily_budget,effective_status,lifetime_budget,name,objective,
                        start_time,status,stop_time,updated_time"""

            params = {"fields": fields,
            "access_token":self.access_token,
            "date_preset": "maximum"
            }
            uri = self.base_url + f"{self.ad_account_id}/{node_name}?"

            data = self.make_get_processing(uri,params)

            if as_df:
                df_data = pd.DataFrame(data)
                return df_data
            else:
                return data

    def get_all_campaigns_insights(self,campaign_id_list):

        full_data = []

        for campaing_id in campaign_id_list:
            campaing_id = str(campaing_id)
            data = self.get_campaign_insights(campaing_id)
            full_data += data

        return full_data



    def get_campaign_insights(self,campaign_id,time_increment=1,as_df=False,date_preset="maximum"):
        fields = """account_currency,account_id,account_name,campaign_id,campaign_name,
            buying_type,clicks,date_start,date_stop,frequency,impressions,
            inline_link_clicks,inline_post_engagement,objective,reach,social_spend,
            spend,unique_clicks,unique_inline_link_clicks,unique_link_clicks_ctr,action_values,
            actions,cost_per_action_type,cost_per_unique_click,
            cpc,cpm,cpp,ctr,purchase_roas,unique_actions,unique_ctr,
            cost_per_thruplay,video_30_sec_watched_actions,
            video_avg_time_watched_actions,video_p100_watched_actions,video_p25_watched_actions,
            video_p50_watched_actions,video_p75_watched_actions,video_p95_watched_actions,video_play_actions"""


        params = {"access_token":self.access_token,
                "fields":fields,
                "date_preset":date_preset,
                "time_increment":time_increment}
        uri = f"{self.base_url}{campaign_id}/insights?"

        data = self.make_get_processing(uri,params)

        if as_df:
            df_data = pd.DataFrame(data)
            return df_data
        else:
            return data

    def get_all_ads_groups(self,as_df=False):
        node_name = "adsets"
        fields = """id,account_id,adlabels,adset_schedule,asset_feed_id,attribution_spec,campaign,campaign_id,created_time,creative_sequence,destination_type,effective_status,end_time,start_time,status,targeting,updated_time"""

        params = {"fields": fields,
        "access_token":self.access_token,
        "date_preset": "maximum"
        }
        uri = self.base_url + f"{self.ad_account_id}/{node_name}?"

        data = self.make_get_processing(uri,params)

        if as_df:
            df_data = pd.DataFrame(data)
            return df_data
        else:
            return data

    def get_adgroups_insights(self,adset_id,time_increment=1,as_df=False,date_preset="maximum"):
        fields = """ad_click_actions,ad_id,ad_impression_actions,ad_name,adset_id,adset_name,age_targeting,
                    campaign_id,clicks,conversions,conversion_values,cpc,cpm,cpp,created_time,ctr,date_start,date_stop,
                    frequency,full_view_impressions,full_view_reach,reach,spend,unique_actions,unique_clicks,updated_time"""


        params = {"access_token":self.access_token,
                "fields":fields,
                "date_preset":date_preset,
                "time_increment":time_increment}
        uri = f"{self.base_url}{adset_id}/insights?"

        data = self.make_get_processing(uri,params)

        if as_df:
            df_data = pd.DataFrame(data)
            return df_data
        else:
            return data


    def get_all_ads(self,as_df=False):
        node_name = "ads"
        fields = """id,account_id,adlabels,created_time,creative,name,status,updated_time"""

        params = {"fields": fields,
        "access_token":self.access_token,
        "date_preset": "maximum"
        }
        uri = self.base_url + f"{self.ad_account_id}/{node_name}?"

        data = self.make_get_processing(uri,params)

        if as_df:
            df_data = pd.DataFrame(data)
            return df_data
        else:
            return data

    def get_ad_insights(self,ad_id,time_increment=1,as_df=False,date_preset="maximum"):
        fields = """account_id,ad_click_actions,ad_id,ad_name,adset_id,age_targeting,campaign_id,clicks,
                    conversions,cpc,cpm,cpp,ctr,date_start,created_time,date_stop,frequency,gender_targeting,
                    impressions,reach,spend,unique_clicks,unique_actions,unique_ctr"""


        params = {"access_token":self.access_token,
                "fields":fields,
                "date_preset":date_preset,
                "time_increment":time_increment}
        uri = f"{self.base_url}{ad_id}/insights?"

        data = self.make_get_processing(uri,params)

        if as_df:
            df_data = pd.DataFrame(data)
            return df_data
        else:
            return data