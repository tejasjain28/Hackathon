import os
import sys
import time
import traceback

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'Common')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Campaign')))
from Common import *
from DB import *

# Variables
Campaign_General = {}

# XPATH
globalSearchContainerXpath = '//div[@data-di-id="global-search-container"]'
globalSearchXPath = "//input[@data-di-id='global-search-search']"
globalSearchAllEntitiesXPath = "//div[@data-di-id='global-search-primaryFilter-select']"
globalSearch_OrdersXPath = "//div[@data-di-id='global-search-menu-item-INSERTION_ORDER-primaryFilter-menuitem']"
globalSearch_CampaignsXPath = "//div[@data-di-id='global-search-menu-item-CAMPAIGN_GROUP-primaryFilter-menuitem']"
globalSearch_AdGroupsXPath = "//div[@data-di-id='global-search-menu-item-CAMPAIGN-primaryFilter-menuitem']"
globalSearch_CreativesXPath = "//div[@data-di-id='global-search-menu-item-CREATIVE-primaryFilter-menuitem']"
globalSearch_AudiencesXPath = "//div[@data-di-id='global-search-menu-item-AUDIENCE-primaryFilter-menuitem']"
globalSearch_OutcomesXPath = "//div[@data-di-id='global-search-menu-item-IMR_REPORT-primaryFilter-menuitem']"
globalSearch_ReportsXPath = "//div[@data-di-id='global-search-menu-item-REPORT-primaryFilter-menuitem']"
globalSearch_DealsXPath = "//div[@data-di-id='global-search-menu-item-DEAL-primaryFilter-menuitem']"
globalSearch_ListsXPath = "//div[@data-di-id='global-search-menu-item-LISTS-primaryFilter-menuitem']"
globalSearch_EverywhereXPath = "//div[@data-di-id='global-search-menu-item-ALL-primaryFilter-menuitem']"

globalSearchAllEntitiesXPath_See_All_Results = "//div[@data-di-id='global-search-primaryFilter-select']"
globalSearch_OrdersXPath_See_All_Results = "//div[@data-di-id='global-search-all-results-menu-item-INSERTION_ORDER-primaryFilter-menuitem']"
globalSearch_CampaignsXPath_See_All_Results = "//div[@data-di-id='global-search-all-results-menu-item-CAMPAIGN_GROUP-primaryFilter-menuitem']"
globalSearch_AdGroupsXPath_See_All_Results = "//div[@data-di-id='global-search-all-results-menu-item-CAMPAIGN-primaryFilter-menuitem']"
globalSearch_CreativesXPath_See_All_Results = "//div[@data-di-id='global-search-all-results-menu-item-CREATIVE-primaryFilter-menuitem']"
globalSearch_AudiencesXPath_See_All_Results = "//div[@data-di-id='global-search-all-results-menu-item-AUDIENCE-primaryFilter-menuitem']"
globalSearch_OutcomesXPath_See_All_Results = "//div[@data-di-id='global-search-all-results-menu-item-IMR_REPORT-primaryFilter-menuitem']"
globalSearch_ReportsXPath_See_All_Results = "//div[@data-di-id='global-search-all-results-menu-item-REPORT-primaryFilter-menuitem']"
globalSearch_DealsXPath_See_All_Results = "//div[@data-di-id='global-search-all-results-menu-item-DEAL-primaryFilter-menuitem']"
globalSearch_ListsXPath_See_All_Results = "//div[@data-di-id='global-search-all-results-menu-item-LISTS-primaryFilter-menuitem']"
globalSearch_EverywhereXPath_See_All_Results = "//div[@data-di-id='global-search-all-results-menu-item-ALL-primaryFilter-menuitem']"

globalSearch_textXPath = "//input[@data-di-id='global-search-search']"
globalSearch_textXPath_See_all = "//input[@data-di-id='global-search-all-results-search']"
global_search_clear_input_xp = '//div[@data-di-id="global-search-modal-close"]|//div[@data-di-id="global-search-all-results-closeIcon"]'
global_search_element_xpath = "//span[(@data-di-id='highlighted-text-container' or @data-di-id='highlighted-bold-text') and text()='{}']/ancestor::p[contains(text(),'{}')]/ancestor::a"


class GlobalSearch:
    def __init__(self):
        try:
            self.pw = BuiltIn().get_library_instance('Browser')
            self.builtlib = BuiltIn().get_library_instance("BuiltIn")
            self.st = BuiltIn().get_library_instance('String')
            self.common = Common()
            self.db = DB()
        except:
            logger.error(sys.exc_info())
            logger.error(traceback.format_exc())

    def selectEntity(self, entityType, see_all_results):
        logger.info(see_all_results)
        if entityType == "Orders":
            if see_all_results != 0:
                self.pw.click(globalSearch_OrdersXPath_See_All_Results)
            else:
                self.pw.click(globalSearch_OrdersXPath)
        elif entityType == "Campaigns":
            if see_all_results != 0:
                self.pw.click(globalSearch_CampaignsXPath_See_All_Results)
            else:
                self.pw.click(globalSearch_CampaignsXPath)
        elif entityType == "Ad Groups":
            if see_all_results != 0:
                self.pw.click(globalSearch_AdGroupsXPath_See_All_Results)
            else:
                self.pw.click(globalSearch_AdGroupsXPath)
        elif entityType == "Creatives":
            if see_all_results != 0:
                self.pw.click(globalSearch_CreativesXPath_See_All_Results)
            else:
                self.pw.click(globalSearch_CreativesXPath)
        elif entityType == "Audiences":
            if see_all_results != 0:
                self.pw.click(globalSearch_AudiencesXPath_See_All_Results)
            else:
                self.pw.click(globalSearch_AudiencesXPath)
        elif entityType == "Outcomes":
            if see_all_results != 0:
                self.pw.click(globalSearch_OutcomesXPath_See_All_Results)
            else:
                self.pw.click(globalSearch_OutcomesXPath)
        elif entityType == "Deals":
            if see_all_results != 0:
                self.pw.click(globalSearch_DealsXPath_See_All_Results)
            else:
                self.pw.click(globalSearch_DealsXPath)
        elif entityType == "Lists":
            if see_all_results != 0:
                self.pw.click(globalSearch_ListsXPath_See_All_Results)
            else:
                self.pw.click(globalSearch_ListsXPath)
        elif entityType == "Report":
            if see_all_results != 0:
                self.pw.click(globalSearch_ReportsXPath_See_All_Results)
            else:
                self.pw.click(globalSearch_ReportsXPath)
        else:
            if see_all_results != 0:
                self.pw.click(globalSearch_EverywhereXPath)
            else:
                self.pw.click(globalSearch_EverywhereXPath_See_All_Results)

    def global_search(self, **kwargs):
        try:
            entityType = kwargs.get('entityType', 'Everywhere')
            subEntityType = kwargs.get('subEntityType', False)
            searchId = kwargs.get('searchId', False)
            searchName = kwargs.get('searchName', False)
            openIn = kwargs.get('openIn', 'SameTab')
            see_all_results = kwargs.get('see_all_results', 0)
            negativeTest=kwargs.get('negativeTest',0)
            advertiser_id = kwargs.get('advertiser_id')
            self.pw.click(globalSearchContainerXpath)
            self.pw.hover(globalSearchXPath)
            self.pw.click(globalSearchXPath)
            self.pw.hover(globalSearchAllEntitiesXPath)
            # self.pw.click(globalSearchAllEntitiesXPath)

            if see_all_results == 0:
                self.selectEntity(entityType, 0)
            else:
                self.selectEntity("Everywhere", 0)
            final_search_text = ""
            if searchName:
                final_search_text = str(searchName)
            elif searchId:
                final_search_text = str(searchId)

            if openIn == "SameTab" and final_search_text:
                time.sleep(5)
                if not int(see_all_results):
                    self.pw.fill_text(globalSearch_textXPath, str(final_search_text))
                    time.sleep(2)
                    if int(negativeTest) == 1:
                        if self.pw.get_element_count(global_search_element_xpath.format(str(final_search_text).strip(), str(subEntityType))):
                            raise Exception (f"{see_all_results} is created before 2022 and still can be searched using global search")
                        else:
                            if 1 == self.pw.get_element_count(global_search_clear_input_xp):
                                self.pw.click(global_search_clear_input_xp)
                            return None
                    else:
                        if entityType == 'Audiences' :
                            logger.info("In not see_all_results")
                            flag = True
                            while flag:
                                if 1 != self.pw.get_element_count('//p[contains(text(), "Audience Group")]/span[@data-di-id="highlighted-text-container"]/span[@data-di-id="highlighted-bold-text" and text()="{}"]/ancestor::p'.format(str(final_search_text).strip())):
                                    new_data_db = f'select distinct(audienceComparisonId) FROM bidder.AUDIENCE_COMPARISON WHERE advertiserId={advertiser_id} and createDate > "2022-12-31 23:59:59" ORDER BY RAND() limit 1;'
                                    db_res = self.db.execute_query(db_query=new_data_db)
                                    final_search_text = db_res[0][0]
                                    logger.info("New Audience Group Id is {}".format(final_search_text))
                                    self.pw.click(globalSearchXPath)
                                    self.pw.clear_text(globalSearchXPath)
                                    self.pw.fill_text(globalSearchXPath,str(final_search_text))
                                    time.sleep(2)
                                    if 1 == self.pw.get_element_count('//p[contains(text(), "Audience Group")]/span[@data-di-id="highlighted-text-container"]/span[@data-di-id="highlighted-bold-text" and text()="{}"]/ancestor::p'.format(str(final_search_text).strip())):
                                        flag = False
                                self.common.click('//p[contains(text(), "Audience Group")]/span[@data-di-id="highlighted-text-container"]/span[@data-di-id="highlighted-bold-text" and text()="{}"]/ancestor::p'.format(str(final_search_text).strip()))
                        else:
                            self.common.retry_click(
                                primary_click_xp="//span[(@data-di-id='highlighted-text-container' or @data-di-id='highlighted-bold-text') and text()='{}']/ancestor::div[@index='0']".format(
                                    str(final_search_text).strip()), defocus_xp="//p[text()='Search']",
                                wait_for_xp="//p[text()='Search']")
                        #self.common.retry_click(
                            # "//span[(@data-di-id='highlighted-text-container' or @data-di-id='highlighted-bold-text') and text()='{}']//parent::span[not(text())][1]".format(
                            #     str(final_search_text).strip()))
                            #"//span[(@data-di-id='highlighted-text-container' or @data-di-id='highlighted-bold-text') and text()='{}']/ancestor::div[@index='0']".format(
                            #    str(final_search_text).strip()))
                else:
                    self.pw.fill_text(globalSearch_textXPath, "qa_")
                    self.pw.click('//div[@data-di-id="global-search-footer"]')
                    self.selectEntity(entityType, int(see_all_results))
                    self.pw.fill_text(globalSearch_textXPath_See_all, str(final_search_text))
                    if subEntityType == 'Audience-group':
                        subEntityType = 'audiences'
                        flag = True
                        while flag:
                            if 1 != self.pw.get_element_count('//p[contains(text(), "Audience Group")]/span[@data-di-id="highlighted-text-container"]/span[@data-di-id="highlighted-bold-text" and text()="{}"]/ancestor::p'.format(
                                    str(final_search_text).strip())):
                                new_data_db = 'select distinct(audienceComparisonId) FROM bidder.AUDIENCE_COMPARISON WHERE advertiserId=10001 and createDate > "2022-12-31 23:59:59" ORDER BY RAND() limit 1;'
                                db_res = self.db.execute_query(new_data_db)
                                final_search_text = db_res[0][0]
                                self.pw.fill_text(globalSearchXPath, final_search_text)
                                time.sleep(2)
                                if 1 == self.pw.get_element_count(
                                    '//p[contains(text(), "Audience Group")]/span[@data-di-id="highlighted-text-container"]/span[@data-di-id="highlighted-bold-text" and text()="{}"]/ancestor::p'.format(
                                        str(final_search_text).strip())):
                                    flag = False
                            self.common.click('//p[contains(text(), "Audience Group")]/span[@data-di-id="highlighted-text-container"]/span[@data-di-id="highlighted-bold-text" and text()="{}"]/ancestor::p'.format(
                                    str(final_search_text).strip()))
                    else:
                        self.pw.click("//span[(@data-di-id='highlighted-text-container' or @data-di-id='highlighted-bold-text') and text()='{}']//parent::span[not(text())][1]".format(
                            str(final_search_text).strip()))
                time.sleep(5)
                self.common.wait_until_xpath_count_equals(count=0, xpath=self.common.data_loading_spinner_xp,
                                                          max_wait_time=30)
            # elif openIn == "SameTab" and final_search_text:
            #     self.pw.fill_text(globalSearch_textXPath, str(final_search_text))
            #     time.sleep(5)
            #     if not int(see_all_results):
            #         self.pw.click(
            #             "//span[(@data-di-id='highlighted-bold-text' or @data-di-id='highlighted-text-container') and text()='{}']".format(
            #                 str(final_search_text).strip()))
            #     else:
            #         self.pw.click('//div[@data-di-id="global-search-footer"]')
            #     time.sleep(5)

            if openIn == "NewTab":
                self.pw.fill_text(globalSearch_textXPath, str(final_search_text))
                time.sleep(5)
                self.pw.click("(//a[@extralinkparams]/*[name()='svg'])[1]/..")
                time.sleep(10)
                # logger.info(self.pw.get_browser_catalog())
                self.pw.switch_page(id="NEW")
                time.sleep(3)
                self.common.wait_until_xpath_count_equals(count=0, xpath=self.common.data_loading_spinner_xp,
                                                          max_wait_time=30)

            current_url = self.pw.get_url()
            if str(entityType) == "Ad Groups":
                self.expand_all_campaign()
                self.search_cli_on_page(final_search_text)
                if not self.pw.get_element_count(f'//label[text()= "{final_search_text}"]'):
                    raise AssertionError("Global Search :: AdGroup not visible in this Url")
            elif subEntityType:
                if str(subEntityType).lower() == "audience-group":
                    subEntityType ='audiences'
                if str(subEntityType).lower() not in str(current_url):
                    raise AssertionError(
                        "Global Search :: Url doesn't contain subEntityType: {}".format(str(subEntityType)))
            elif str(entityType).lower() not in str(current_url):
                raise AssertionError("Global Search :: Url doesn't contain entityType: {}".format(str(entityType)))

            if 1 == self.pw.get_element_count(global_search_clear_input_xp):
                self.pw.click(global_search_clear_input_xp)

        except:
            logger.error("Function :global_search failed.")
            tb = traceback.format_exc()
            self.pw.take_screenshot()
            raise Exception(tb)
        finally:
            logger.info("global_search Function Completed")

    def expand_all_campaign(self):
        try:
            count=self.pw.get_element_count('(//span[@class="ag-group-contracted "])[1]')
            logger.info(f"count{count}")
            for i in range(1,count+1):
                self.pw.click('(//span[@class="ag-group-contracted "])[1]')
        except Exception as e:
            logger.error("expand_all_campaign Function failed.")
            self.pw.take_screenshot()
            raise Exception(e)
        finally:
            logger.info("expand_all_campaign Function Completed")

    def search_cli_on_page(self, cli_id):
        try:
            search_name_xpath='//input[@aria-label="Name Filter Input"]'
            self.common.wait_until_xpath_count_equals(count=0, xpath=self.common.data_loading_spinner_xp,
                                                      max_wait_time=20)
            self.pw.click(search_name_xpath)
            self.pw.fill_text(search_name_xpath, str(cli_id))
        except Exception as e:
            logger.error("search_and_edit_cli Function Failed")
            self.pw.take_screenshot()
            logger.error(traceback.format_exc())
            raise Exception(e)
        finally:
            logger.info("Exit search_and_edit_cli")
    def global_search_using_shortcuts(self, **kwargs):
        try:
            entityType = kwargs.get('entityType', 'Orders')
            searchId = kwargs.get('searchId', False)
            searchName = kwargs.get('searchName', False)
            openIn = kwargs.get('openIn', 'SameTab')
            see_all_results = kwargs.get('see_all_results', 0)
            self.pw.press_keys("//body", '/')
            self.pw.hover(globalSearchAllEntitiesXPath)
            self.selectEntity(entityType, 0)
            final_search_text = ""
            if searchName:
                final_search_text = str(searchName)
            elif searchId:
                final_search_text = str(searchId)

            if openIn == "SameTab" and final_search_text:
                time.sleep(5)
                if not int(see_all_results):
                    self.pw.fill_text(globalSearch_textXPath, str(final_search_text))
                    time.sleep(5)
                    self.pw.press_keys("//body", 'ArrowDown')
                    time.sleep(5)
                    self.pw.press_keys("//body", 'Enter')
                else:
                    self.pw.fill_text(globalSearch_textXPath, "qa_")
                    self.pw.click('//div[@data-di-id="global-search-footer"]')
                    self.selectEntity(entityType, int(see_all_results))
                    self.pw.fill_text(globalSearch_textXPath_See_all, str(final_search_text))
                    self.pw.click(
                        "//span[(@data-di-id='highlighted-text-container' or @data-di-id='highlighted-bold-text') and text()='{}']//parent::span[not(text())][1]".format(
                            str(final_search_text).strip()))
                time.sleep(5)
            current_url = self.pw.get_url()
            if str(entityType).lower() not in str(current_url):
                raise AssertionError("Global Search :: Url doesn't contain entityType: {}".format(str(entityType)))

        except:
            logger.error("Function :global_search failed.")
            tb = traceback.format_exc()
            self.pw.take_screenshot()
            raise Exception(tb)
        finally:
            logger.info("global_search Function Completed")

    def unshare_dealGroup_and_check_RecentSearch(self,**kwargs):
        try:
            dealGroupSharingId=kwargs.get('dealGroupSharingId')
            dealGroupId=kwargs.get('dealGroupId')
            query = f"select dealGroupId,organizationId,advertiserId from marketplace.DEAL_GROUP_SHARING where dealGroupSharingId={dealGroupSharingId}"
            response1 = self.db.execute_query(db_query=query)
            query=f"delete from marketplace.DEAL_GROUP_SHARING where dealGroupSharingId={dealGroupSharingId}"
            response2 =self.db.execute_query(db_query=query)
            self.pw.click(globalSearchContainerXpath)
            self.pw.hover(globalSearchXPath)
            self.pw.click(globalSearchXPath)
            time.sleep(10)
            if self.pw.get_element_count(f"//span[@data-di-id='highlighted-text-container' and text()='{dealGroupId}']"):
                raise Exception("Unshared DealGroup Id did not get removed from recent searches")
            query = f"insert into marketplace.DEAL_GROUP_SHARING (dealGroupId,organizationId,advertiserId) values {response1[0]}"
            self.pw.click(global_search_clear_input_xp)
            response = self.db.execute_query(db_query=query)
        except:
            logger.error("Function :unshare_dealGroup_and_check_RecentSearch failed.")
            tb = traceback.format_exc()
            self.pw.take_screenshot()
            raise Exception(tb)
        finally:
            logger.info("unshare_dealGroup_and_check_RecentSearch Function Completed")
