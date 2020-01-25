#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dallasparser.regex import *
from dallasparser.utils import *

from openpyxl import load_workbook
from dateutil.parser import parse
from bs4 import BeautifulSoup
from tqdm import tqdm
import unicodedata
import pandas as pd
import sys
import csv
import re
import os

class TXDallasParser:
	COLUMN_ORDER = {
		'judicial_information': JUDICIAL_HEADERS,
		'sets_and_passes': SETS_HEADERS,
		'names': NAMES_HEADERS,
		'bonds': BONDS_HEADERS,
		'charges': CHARGES_HEADERS,
		'dispositions': DISPOSITIONS_HEADERS,
		'reduced_enhanced_charges': RED_ENH_HEADERS,
		'general_comments': GC_HEADERS,
		'general_comments_ws_date': GC_WS_DATE_HEADERS,
		'motions': MOTIONS_HEADERS,
		'probation_revocation': PROB_REVOC_HEADERS,
		'appeals': APPEALS_HEADERS,
		'competency_data': COMPETENCY_HEADERS,
		'payments': PAYMENTS_HEADERS,
		'bond_comments': BOND_COMMENTS_HEADERS
	}
	def __init__(self, input_path=None, output_path=None):
		self.input_path = input_path
		self.output_path = output_path

	def extract_tables(self, trs):
		IS_JUDICIAL = False
		IS_BOND = False
		IS_SETS = False
		IS_NAMES = False
		IS_CHARGE = False
		IS_DISP = False
		IS_RED_ENH = False
		IS_COMMENT = False
		IS_COMMENT_WS = False
		IS_MOTION = False
		IS_PROB_REVOC = False
		IS_APPEAL = False
		IS_COMP = False
		IS_PAYMENT = False
		IS_BOND_COMMENT = False

		JUDICIAL_TRS = list()
		BONDS_TRS = list()
		SETS_TRS = list()
		NAMES_TRS = list()
		CHARGE_TRS = list()
		DISP_TRS = list()
		RED_ENH_TRS = list()
		COMMENT_TRS = list()
		COMMENT_WS_TRS = list()
		MOTION_TRS = list()
		PROB_REVOC_TRS = list()
		APPEAL_TRS = list()
		COMP_TRS = list()
		PAYMENT_TRS = list()
		BOND_COMMENT_TRS = list()

		for tr in trs:
			if tr.td.b is not None:
				header = re.sub(r'\s+', '', tr.text.strip())
				if header=='JUDICIALINFORMATION': IS_JUDICIAL = True
				else: IS_JUDICIAL = False
				if header=='BONDS': IS_BOND = True
				else: IS_BOND = False
				if header=='SETSANDPASSES': IS_SETS = True
				else: IS_SETS = False
				if header=='NAMES': IS_NAMES = True
				else: IS_NAMES = False
				if header=='CHARGE': IS_CHARGE = True
				else: IS_CHARGE = False
				if header=='DISPOSITION': IS_DISP = True
				else: IS_DISP = False
				if header=='REDUCED/ENHANCEDCHARGE': IS_RED_ENH = True
				else: IS_RED_ENH = False
				if header=='GENERALCOMMENTS': IS_COMMENT = True
				else: IS_COMMENT = False
				if header=='GENERALCOMMENTSWSDATE': IS_COMMENT_WS = True
				else: IS_COMMENT_WS = False
				if header=='MOTIONS': IS_MOTION = True
				else: IS_MOTION = False
				if header=='PROBATIONREVOCATION': IS_PROB_REVOC = True
				else: IS_PROB_REVOC = False
				if header=='APPEALS': IS_APPEAL = True
				else: IS_APPEAL = False
				if header=='COMPETENCYDATA' or header=='BAILBONDHEARING/COMPETENCYDATA': IS_COMP = True
				else: IS_COMP = False
				if header=='PAYMENTS': IS_PAYMENT = True
				else: IS_PAYMENT = False
				if header=='BONDCOMMENTS': IS_BOND_COMMENT = True
				else: IS_BOND_COMMENT = False
			else:
				content = unicodedata.normalize('NFKD', tr.text.strip())
				if IS_JUDICIAL: JUDICIAL_TRS.append(content)
				elif IS_SETS: SETS_TRS.append(content)
				elif IS_NAMES: NAMES_TRS.append(content)
				elif IS_BOND: BONDS_TRS.append(content)
				elif IS_CHARGE: CHARGE_TRS.append(content)
				elif IS_DISP: DISP_TRS.append(content)
				elif IS_RED_ENH: RED_ENH_TRS.append(content)
				elif IS_COMMENT: COMMENT_TRS.append(content)
				elif IS_COMMENT_WS: COMMENT_WS_TRS.append(content)
				elif IS_MOTION: MOTION_TRS.append(content)
				elif IS_PROB_REVOC: PROB_REVOC_TRS.append(content)
				elif IS_APPEAL: APPEAL_TRS.append(content)
				elif IS_COMP: COMP_TRS.append(content)
				elif IS_PAYMENT: PAYMENT_TRS.append(content)
				elif IS_BOND_COMMENT: BOND_COMMENT_TRS.append(content)
		return (JUDICIAL_TRS, SETS_TRS, NAMES_TRS, BONDS_TRS, CHARGE_TRS,
				DISP_TRS, RED_ENH_TRS, COMMENT_TRS, COMMENT_WS_TRS,
				MOTION_TRS, PROB_REVOC_TRS, APPEAL_TRS, COMP_TRS,
				PAYMENT_TRS, BOND_COMMENT_TRS)

	def get_judicial_information(self, judicial_trs, da_case_id, jd_case_id):
		DATA_DICT = dict()
		DATA_DICT['da_case_id'] = da_case_id
		DATA_DICT['jd_case_id'] = jd_case_id

		### JUDICIAL_TRS[0]
		DEF_NAME = DEF_NAME_REGEX.search(judicial_trs[0]).group().strip()
		DEF_RACE = DEF_RACE_REGEX.search(judicial_trs[0]).group().strip()
		DEF_SEX = DEF_SEX_REGEX.search(judicial_trs[0]).group().strip()
		DEF_DOB = DEF_DOB_REGEX.search(judicial_trs[0]).group().strip()
		DEF_AGE = DEF_AGE_REGEX.search(judicial_trs[0]).group().strip()
		name = clean_val(DEF_NAME)
		DATA_DICT['name_raw'] = name
		DATA_DICT['race'] = clean_val(DEF_RACE)
		DATA_DICT['sex'] = clean_val(DEF_SEX)
		DATA_DICT['dob'] = clean_val(DEF_DOB)
		DATA_DICT['age'] = clean_val(DEF_AGE)

		### JUDICIAL_TRS[1]
		DEF_ADDR = DEF_ADDR_REGEX.search(judicial_trs[1]).group().strip()
		DEF_AC = DEF_AC_REGEX.search(judicial_trs[1]).group().strip()
		DEF_PH = DEF_PH_REGEX.search(judicial_trs[1]).group().strip()
		DEF_SS = DEF_SS_REGEX.search(judicial_trs[1]).group().strip()
		DATA_DICT['def_adr1'] = clean_val(DEF_ADDR)
		DATA_DICT['ac'] = clean_val(DEF_AC)
		DATA_DICT['ph'] = clean_val(DEF_PH)
		DATA_DICT['ss'] = clean_val(DEF_SS)

		### JUDICIAL_TRS[2]
		DEF_CITY = DEF_CITY_REGEX.search(judicial_trs[2]).group().strip()
		DEF_STATE = DEF_STATE_REGEX.search(judicial_trs[2]).group().strip()
		DEF_ZIP = DEF_ZIP_REGEX.search(judicial_trs[2]).group().strip()
		DEF_DL_NUM = DEF_DL_NUM_REGEX.search(judicial_trs[2]).group().strip()
		DEF_DL_STATE = DEF_DL_STATE_REGEX.search(judicial_trs[2]).group().strip()
		DATA_DICT['city'] = clean_val(DEF_CITY)
		DATA_DICT['state'] = clean_val(DEF_STATE)
		DATA_DICT['zip'] = clean_val(DEF_ZIP)
		DATA_DICT['dl_number'] = clean_val(DEF_DL_NUM)
		DATA_DICT['dl_state'] = clean_val(DEF_DL_STATE)

		### JUDICIAL_TRS[3]
		DEF_OFF = DEF_OFF_REGEX.search(judicial_trs[3]).group().strip()
		DEF_OFF_DT = DEF_OFF_DT_REGEX.search(judicial_trs[3]).group().strip()
		DEF_OFF_TYP_CLS = DEF_OFF_TYP_CLS_REGEX.search(judicial_trs[3]).group().strip().split()
		DEF_OFF_TYPE = DEF_OFF_TYP_CLS[0].strip()
		DEF_OFF_CLS = DEF_OFF_TYP_CLS[1].strip()
		DEF_OFF_GOC_CAT = DEF_OFF_GOC_CAT_REGEX.search(judicial_trs[3]).group().strip().split()
		DEF_OFF_GOC = DEF_OFF_GOC_CAT[0].strip()
		DEF_OFF_CAT = DEF_OFF_GOC_CAT[1].strip()
		DEF_OFF_CODE = DEF_OFF_CODE_REGEX.search(judicial_trs[3]).group().strip()
		DATA_DICT['offense'] = clean_val(DEF_OFF)
		DATA_DICT['offense_date'] = clean_val(DEF_OFF_DT)
		DATA_DICT['offense_type'] = clean_val(DEF_OFF_TYPE)
		DATA_DICT['offense_class'] = clean_val(DEF_OFF_CLS)
		DATA_DICT['goc'] = clean_val(DEF_OFF_GOC)
		DATA_DICT['cat'] = clean_val(DEF_OFF_CAT)
		DATA_DICT['offense_code'] = clean_val(DEF_OFF_CODE)

		### JUDICIAL_TRS[4]
		DEF_COMT = DEF_COMT_REGEX.search(judicial_trs[4]).group().strip()
		DEF_SID_NUM = DEF_SID_NUM_REGEX.search(judicial_trs[4]).group().strip()
		try:
			DEF_OF_AMT = DEF_OF_AMT_REGEX.search(judicial_trs[4]).group().strip()
		except AttributeError:
			DEF_OF_AMT = ''
		DATA_DICT['comt'] = clean_val(DEF_COMT)
		DATA_DICT['sid_number'] = clean_val(DEF_SID_NUM)
		DATA_DICT['of_amt'] = clean_val(DEF_OF_AMT)

		### JUDICIAL_TRS[5]
		DEF_COMPLAINANT = DEF_COMPLAINANT_REGEX.search(judicial_trs[5]).group().strip()
		DEF_TAPE_NUM = DEF_TAPE_NUM_REGEX.search(judicial_trs[5]).group().strip()
		DEF_ARREST_DATE = DEF_ARREST_DATE_REGEX.search(judicial_trs[5]).group().strip()
		DATA_DICT['complainant'] = clean_val(DEF_COMPLAINANT)
		DATA_DICT['tape_number'] = clean_val(DEF_TAPE_NUM)
		DATA_DICT['arrest_date'] = clean_val(DEF_ARREST_DATE)

		### JUDICIAL_TRS[6]
		DEF_JUV_STAT = DEF_JUV_STAT_REGEX.search(judicial_trs[6]).group().strip()
		DEF_REPEAT_STAT = DEF_REPEAT_STAT_REGEX.search(judicial_trs[6]).group().strip()
		DEF_CAREER_STAT = DEF_CAREER_STAT_REGEX.search(judicial_trs[6]).group().strip()
		DEF_ORIG_LOC = DEF_ORIG_LOC_REGEX.search(judicial_trs[6]).group().strip()
		DEF_CURR_LOC = DEF_CURR_LOC_REGEX.search(judicial_trs[6]).group().strip()
		DATA_DICT['juvenile_status'] = clean_val(DEF_JUV_STAT)
		DATA_DICT['repeat_offender'] = clean_val(DEF_REPEAT_STAT)
		DATA_DICT['career_offender'] = clean_val(DEF_CAREER_STAT)
		DATA_DICT['orig_loc'] = clean_val(DEF_ORIG_LOC)
		DATA_DICT['curr_loc'] = clean_val(DEF_CURR_LOC)

		### JUDICIAL_TRS[7]
		DEF_FILING_AGENCY = DEF_FILING_AGENCY_REGEX.search(judicial_trs[7]).group().strip()
		DEF_SER_CASE_NUM = DEF_SER_CASE_NUM_REGEX.search(judicial_trs[7]).group().strip()
		DEF_ARREST_NUM = DEF_ARREST_NUM_REGEX.search(judicial_trs[7]).group().strip()
		DATA_DICT['filing_agency'] = clean_val(DEF_FILING_AGENCY)
		DATA_DICT['ser_cas_number'] = clean_val(DEF_SER_CASE_NUM)
		DATA_DICT['arrest_number'] = clean_val(DEF_ARREST_NUM)

		### JUDICIAL_TRS[8]
		DEF_LAI_NUM = DEF_LAI_NUM_REGEX.search(judicial_trs[8]).group().strip()
		DEF_AIS_DSO_NUM = DEF_AIS_DSO_NUM_REGEX.search(judicial_trs[8]).group().strip()
		DEF_BOOKING_NUM = DEF_BOOKING_NUM_REGEX.search(judicial_trs[8]).group().strip()
		DATA_DICT['lai_number'] = clean_val(DEF_LAI_NUM)
		DATA_DICT['ais_dso_number'] = clean_val(DEF_AIS_DSO_NUM)
		DATA_DICT['booking_number'] = clean_val(DEF_BOOKING_NUM)

		### JUDICIAL_TRS[9]
		DEF_JP_FILE_DATE = DEF_JP_FILE_DATE_REGEX.search(judicial_trs[9]).group().strip()
		DEF_JP_CASE_ID = DEF_JP_CASE_ID_REGEX.search(judicial_trs[9]).group().strip()
		DEF_JP_COURT_ID = DEF_JP_COURT_ID_REGEX.search(judicial_trs[9]).group().strip()
		DEF_FED = DEF_FED_REGEX.search(judicial_trs[9]).group().strip()
		DEF_EVH = DEF_EVH_REGEX.search(judicial_trs[9]).group().strip()
		DEF_AFF = DEF_AFF_REGEX.search(judicial_trs[9]).group().strip()
		DATA_DICT['jp_file_date'] = clean_val(DEF_JP_FILE_DATE)
		DATA_DICT['jp_case_id'] = clean_val(DEF_JP_CASE_ID)
		DATA_DICT['jp_court_id'] = clean_val(DEF_JP_COURT_ID)
		DATA_DICT['fed'] = clean_val(DEF_FED)
		DATA_DICT['evh'] = clean_val(DEF_EVH)
		DATA_DICT['aff'] = clean_val(DEF_AFF)

		### JUDICIAL_TRS[10]
		DEF_MAGIS_DATE = DEF_MAGIS_DATE_REGEX.search(judicial_trs[10]).group().strip()
		DEF_MAGIS_COURT = DEF_MAGIS_COURT_REGEX.search(judicial_trs[10]).group().strip()
		DEF_MAGIS_JUDGE = DEF_MAGIS_JUDGE_REGEX.search(judicial_trs[10]).group().strip()
		DEF_BOUND_OVER = DEF_BOUND_OVER_REGEX.search(judicial_trs[10]).group().strip()
		DATA_DICT['magistrate_date'] = clean_val(DEF_MAGIS_DATE)
		DATA_DICT['magis_court'] = clean_val(DEF_MAGIS_COURT)
		DATA_DICT['magis_judge'] = clean_val(DEF_MAGIS_JUDGE)
		DATA_DICT['bound_over'] = clean_val(DEF_BOUND_OVER)

		### JUDICIAL_TRS[11]
		DEF_EXAM_TRIAL_DATE = DEF_EXAM_TRIAL_DATE_REGEX.search(judicial_trs[11]).group().strip()
		DEF_EXAM_COURT = DEF_EXAM_COURT_REGEX.search(judicial_trs[11]).group().strip()
		DEF_EXAM_JUDGE = DEF_EXAM_JUDGE_REGEX.search(judicial_trs[11]).group().strip()
		DEF_IND_METHOD = DEF_IND_METHOD_REGEX.search(judicial_trs[11]).group().strip()
		DATA_DICT['exam_trial_date'] = clean_val(DEF_EXAM_TRIAL_DATE)
		DATA_DICT['exam_court'] = clean_val(DEF_EXAM_COURT)
		DATA_DICT['exam_judge'] = clean_val(DEF_EXAM_JUDGE)
		DATA_DICT['ind_meth'] = clean_val(DEF_IND_METHOD)

		### JUDICIAL_TRS[12]
		DEF_GJ_H_R_DATE = DEF_GJ_H_R_DATE_REGEX.search(judicial_trs[12]).group().strip()
		DEF_GJ_NUM = DEF_GJ_NUM_REGEX.search(judicial_trs[12]).group().strip()
		DEF_GJ_W_FILE_DATE = DEF_GJ_W_FILE_DATE_REGEX.search(judicial_trs[12]).group().strip()
		DEF_GJ_DS = DEF_GJ_DS_REGEX.search(judicial_trs[12]).group().strip()
		DEF_DA_DSP = DEF_DA_DSP_REGEX.search(judicial_trs[12]).group().strip()
		DEF_ACC = DEF_ACC_REGEX.search(judicial_trs[12]).group().strip()
		DEF_REAS = DEF_REAS_REGEX.search(judicial_trs[12]).group().strip()
		DATA_DICT['gj_h_r_date'] = clean_val(DEF_GJ_H_R_DATE)
		DATA_DICT['gj_number'] = clean_val(DEF_GJ_NUM)
		DATA_DICT['gj_w_file'] = clean_val(DEF_GJ_W_FILE_DATE)
		DATA_DICT['gj_ds'] = clean_val(DEF_GJ_DS)
		DATA_DICT['da_dsp'] = clean_val(DEF_DA_DSP)
		DATA_DICT['acc'] = clean_val(DEF_ACC)
		DATA_DICT['reas'] = clean_val(DEF_REAS)

		### JUDICIAL_TRS[13]
		DEF_DA_DISP_DATE = DEF_DA_DISP_DATE_REGEX.search(judicial_trs[13]).group().strip()
		DEF_MISD_REDUC = DEF_MISD_REDUC_REGEX.search(judicial_trs[13]).group().strip()
		DEF_SENT_PROB = DEF_SENT_PROB_REGEX.search(judicial_trs[13]).group().strip()
		DATA_DICT['da_dispos_date'] = clean_val(DEF_DA_DISP_DATE)
		DATA_DICT['misdemeanor_reduction'] = clean_val(DEF_MISD_REDUC)
		DATA_DICT['sentence_probated'] = clean_val(DEF_SENT_PROB)

		### JUDICIAL_TRS[14]
		DEF_JUDCL_CASE_ID = DEF_JUDCL_CASE_ID_REGEX.search(judicial_trs[14]).group().strip()
		DEF_GJ_CT = DEF_GJ_CT_REGEX.search(judicial_trs[14]).group().strip()
		DEF_PROS_STATE = DEF_PROS_STAT_REGEX.search(judicial_trs[14]).group().strip()
		DEF_PROS_NAME = DEF_PROS_NAME_REGEX.search(judicial_trs[14]).group().strip()
		DATA_DICT['judcl_case_id'] = clean_val(DEF_JUDCL_CASE_ID)
		DATA_DICT['gj_ct'] = clean_val(DEF_GJ_CT)
		DATA_DICT['pros_stat'] = clean_val(DEF_PROS_STATE)
		DATA_DICT['pros_name'] = clean_val(DEF_PROS_NAME)

		### JUDICIAL_TRS[15]
		DEF_COURT_ASSIGNED = DEF_COURT_ASSIGNED_TO_REGEX.search(judicial_trs[15]).group().strip()
		DEF_DATE_ASSIGNED = DEF_DATE_ASSIGNED_REGEX.search(judicial_trs[15]).group().strip()
		DEF_ASSIGNED_BY = DEF_ASSIGNED_BY_REGEX.search(judicial_trs[15]).group().strip()
		DEF_REASON = DEF_REASON_REGEX.search(judicial_trs[15]).group().strip()
		DATA_DICT['court_assigned_to'] = clean_val(DEF_COURT_ASSIGNED)
		DATA_DICT['date_assigned'] = clean_val(DEF_DATE_ASSIGNED)
		DATA_DICT['assigned_by'] = clean_val(DEF_ASSIGNED_BY)
		DATA_DICT['reason'] = clean_val(DEF_REASON)

		### JUDICIAL_TRS[16]
		DEF_PRE_CASE_ID = DEF_PRE_CASE_ID_REGEX.search(judicial_trs[16]).group().strip()
		DEF_SUC_CASE_ID = DEF_SUC_CASE_ID_REGEX.search(judicial_trs[16]).group().strip()
		DATA_DICT['preceeding_da_case_id'] = clean_val(DEF_PRE_CASE_ID)
		DATA_DICT['succeeding_da_case_id'] = clean_val(DEF_SUC_CASE_ID)

		### JUDICIAL_TRS[17]
		DEF_TRN = DEF_TRN_REGEX.search(judicial_trs[17]).group().strip()
		DEF_TRS = DEF_TRS_REGEX.search(judicial_trs[17]).group().strip()
		DEF_WARR_STAT = DEF_WARR_STAT_REGEX.search(judicial_trs[17]).group().strip()
		DEF_STATE_OFF_CD = DEF_STATE_OFF_CD_REGEX.search(judicial_trs[17]).group().strip()
		DATA_DICT['trn'] = clean_val(DEF_TRN)
		DATA_DICT['trs'] = clean_val(DEF_TRS)
		DATA_DICT['warrant_status'] = clean_val(DEF_WARR_STAT)
		DATA_DICT['state_offense_code'] = clean_val(DEF_STATE_OFF_CD)

		return DATA_DICT

	def get_sets_and_passes(self, sets_trs, da_case_id, jd_case_id):
		sp_id = 0
		DATA_LIST = list()
		DATA_DICT = dict()
		for content in sets_trs:
			if SET_DATE_REGEX.search(content):
				if len(DATA_DICT.keys())>0:
					DATA_LIST.append(DATA_DICT)
					DATA_DICT = dict()
				sp_id += 1
				DATA_DICT['sp_id'] = sp_id
				DATA_DICT['da_case_id'] = da_case_id
				DATA_DICT['jd_case_id'] = jd_case_id
				SET_DATE = SET_DATE_REGEX.search(content).group().strip()
				SET_TIME = SET_TIME_REGEX.search(content).group().strip()
				SET_TYPE = SET_TYPE_REGEX.search(content).group().strip()
				PASSED_DT = SET_PASSED_DATE_REGEX.search(content).group().strip()
				DATA_DICT['set_for_date'] = clean_val(SET_DATE)
				DATA_DICT['set_for_time'] = clean_val(SET_TIME)
				DATA_DICT['set_type'] = clean_val(SET_TYPE)
				DATA_DICT['passed_to_date'] = clean_val(PASSED_DT)
			elif SET_DISP_CODE_REGEX.search(content):
				DISP_CODE = SET_DISP_CODE_REGEX.search(content).group().strip()
				PASS_GEN = SET_PASS_GEN_REGEX.search(content).group().strip()
				COMMENTS = SET_COMMENTS_REGEX.search(content).group().strip()
				DATA_DICT['set_disposition_code'] = clean_val(DISP_CODE)
				DATA_DICT['passed_generally'] = clean_val(PASS_GEN)
				DATA_DICT['comments'] = clean_val(COMMENTS)
			elif SET_STATES_REC_REGEX.search(content):
				STATE_REC = SET_STATES_REC_REGEX.search(content).group().strip()
				REC_NO = SET_REC_NUM_REGEX.search(content).group().strip()
				DATA_DICT['states_recommendation'] = clean_val(STATE_REC)
				DATA_DICT['rec_no'] = clean_val(REC_NO)
		DATA_LIST.append(DATA_DICT)
		return DATA_LIST

	def get_names(self, names_trs, da_case_id, jd_case_id):
		name_id = 0
		DATA_LIST = list()
		DATA_DICT = dict()
		for content in names_trs:
			if NAME_ASSOC_REGEX.search(content):
				if len(DATA_DICT.keys())>0:
					DATA_LIST.append(DATA_DICT)
					DATA_DICT = dict()
				name_id += 1
				DATA_DICT['name_id'] = name_id
				DATA_DICT['da_case_id'] = da_case_id
				DATA_DICT['jd_case_id'] = jd_case_id
				ASSOC_NAME = NAME_ASSOC_REGEX.search(content).group().strip()
				NAME_CODE = NAME_REF_CODE_REGEX.search(content).group().strip()
				DATA_DICT['associated_name'] = clean_val(ASSOC_NAME)
				DATA_DICT['name_ref_code'] = clean_val(NAME_CODE)
			else:
				CT_APPT = NAME_CT_APPT_REGEX.search(content).group().strip()
				BAR_NO = NAME_BAR_NO_REGEX.search(content).group().strip()
				BONDER = NAME_BOND_MAKER_REGEX.search(content).group().strip()
				BOND = NAME_BOND_MADE_REGEX.search(content).group().strip()
				DATA_DICT['ct_appointed'] = clean_val(CT_APPT)
				DATA_DICT['bar_no'] = clean_val(BAR_NO)
				DATA_DICT['bond_maker'] = clean_val(BONDER)
				DATA_DICT['dt_bond_made'] = clean_val(BOND)
		DATA_LIST.append(DATA_DICT)
		return DATA_LIST

	def get_bonds(self, bonds_trs, da_case_id, jd_case_id):
		bond_id = 0
		DATA_LIST = list()
		DATA_DICT = dict()
		for content in bonds_trs:
			if BOND_DATE_SET_REGEX.search(content):
				if len(DATA_DICT.keys())>0:
					DATA_LIST.append(DATA_DICT)
					DATA_DICT = dict()
				bond_id += 1
				DATA_DICT['bond_id'] = bond_id
				DATA_DICT['da_case_id'] = da_case_id
				DATA_DICT['jd_case_id'] = jd_case_id
				DATE_SET = BOND_DATE_SET_REGEX.search(content).group().strip()
				AMT = BOND_AMT_REGEX.search(content).group().strip()
				TYPE = BOND_TYPE_REGEX.search(content).group().strip()
				SET_BY = BOND_SET_BY_REGEX.search(content).group().strip()
				JUDGE = BOND_JUDGE_REGEX.search(content).group().strip()
				DATA_DICT['date_bond_set'] = clean_val(DATE_SET)
				DATA_DICT['amt'] = clean_val(AMT)
				DATA_DICT['type'] = clean_val(TYPE)
				DATA_DICT['set_by_court'] = clean_val(SET_BY)
				DATA_DICT['judge'] = clean_val(JUDGE)
			elif BOND_REC_NO_REGEX.search(content):
				REC_NO = BOND_REC_NO_REGEX.search(content).group().strip()
				DATA_DICT['rec_no'] = clean_val(REC_NO)
		DATA_LIST.append(DATA_DICT)
		return DATA_LIST

	def get_charges(self, charge_trs, da_case_id, jd_case_id):
		DATA_LIST = list()
		DATA_DICT = dict()
		charge_id = 0
		for content in charge_trs:
			if CHRG_NAME_REGEX.search(content):
				if len(DATA_DICT.keys())>0:
					DATA_LIST.append(DATA_DICT)
					DATA_DICT = dict()
				charge_id += 1
				DATA_DICT['charge_id'] = charge_id
				DATA_DICT['da_case_id'] = da_case_id
				DATA_DICT['jd_case_id'] = jd_case_id
				CHRG_NAME = CHRG_NAME_REGEX.search(content).group().strip()
				OFF_CD = CHRG_OFF_CD_REGEX.search(content).group().strip()
				STATE_CD = CHRG_STATE_CD_REGEX.search(content).group().strip()
				DATA_DICT['name_raw'] = clean_val(CHRG_NAME)
				DATA_DICT['offense_cd'] = clean_val(OFF_CD)
				DATA_DICT['state_cd'] = clean_val(STATE_CD)
			elif CHRG_DESC_REGEX.search(content):
				DESC = CHRG_DESC_REGEX.search(content).group().strip()
				COMT = CHRG_COMT_REGEX.search(content).group().strip()
				TYPE_CL = CHRG_TYPE_CL_REGEX.search(content).group().strip().split()
				try:
					GOC = CHRG_GOC_REGEX.search(content).group().strip()
				except AttributeError:
					GOC = ''
				DATA_DICT['offense_desc'] = clean_val(DESC)
				DATA_DICT['comt'] = clean_val(COMT)
				if len(TYPE_CL)==2:
					DATA_DICT['offense_type'] = clean_val(TYPE_CL[0]).strip()
					DATA_DICT['offense_class'] = clean_val(TYPE_CL[1]).strip()
				else:
					DATA_DICT['offense_type'] = clean_val(TYPE_CL[0]).strip()
				DATA_DICT['goc'] = clean_val(GOC)
			elif CHRG_GJ_CT_REGEX.search(content):
				GJ_CT = CHRG_GJ_CT_REGEX.search(content).group().strip()
				CURR_CT = CHRG_CURR_CT_REGEX.search(content).group().strip()
				PREV_CT = CHRG_PREV_CT_REGEX.search(content).group().strip()
				try:
					CHOV_DT = CHRG_CHOV_DT_REGEX.search(content).group().strip()
				except AttributeError:
					CHOV_DT = ''
				DATA_DICT['gj_court'] = clean_val(GJ_CT)
				DATA_DICT['current_court'] = clean_val(CURR_CT)
				DATA_DICT['previous_courts'] = clean_val(PREV_CT)
				DATA_DICT['chov_dt'] = clean_val(CHOV_DT)
		DATA_LIST.append(DATA_DICT)
		return DATA_LIST

	def get_dispositions(self, disp_trs, da_case_id, jd_case_id):
		disp_id = 0
		DATA_LIST = list()
		DATA_DICT = dict()

		for content in disp_trs:
			if DISP_NO_REGEX.search(content):
				if len(DATA_DICT.keys())>0:
					DATA_LIST.append(DATA_DICT)
					DATA_DICT = dict()
				disp_id += 1
				DISP_NO = DISP_NO_REGEX.search(content).group().strip()
				DATA_DICT['ct_disp_no'] = clean_val(DISP_NO)
				DATA_DICT['da_case_id'] = da_case_id
				DATA_DICT['jd_case_id'] = jd_case_id
				DATA_DICT['disp_id'] = disp_id
			elif DISP_VERDICT_DATE_REGEX.search(content):
				VERDICT_DATE = DISP_VERDICT_DATE_REGEX.search(content).group().strip()
				VERDICT_BY = DISP_VERDICT_BY_REGEX.search(content).group().strip()
				VERDICT_JG = DISP_VERDICT_JG_REGEX.search(content).group().strip()
				TC = DISP_TC_REGEX.search(content).group().strip()
				DISM_TYPE = DISP_DISM_TYP_REGEX.search(content).group().strip()
				VERDICT_VOL = DISP_VERDICT_VOL_REGEX.search(content).group().strip()
				VERDICT_PAGE = DISP_VERDICT_PAGE_REGEX.search(content).group().strip()
				DATA_DICT['verdict_date'] = clean_val(VERDICT_DATE)
				DATA_DICT['verdict_by'] = clean_val(VERDICT_BY)
				DATA_DICT['verdict_jg'] = clean_val(VERDICT_JG)
				DATA_DICT['verdict_tc'] = clean_val(TC)
				DATA_DICT['dism_type'] = clean_val(DISM_TYPE)
				DATA_DICT['verdict_vol'] = clean_val(VERDICT_VOL)
				DATA_DICT['verdict_page'] = clean_val(VERDICT_PAGE)
			elif DISP_SENT_DATE_REGEX.search(content):
				SENT_DATE = DISP_SENT_DATE_REGEX.search(content).group().strip()
				SENT_BY = DISP_SENT_BY_REGEX.search(content).group().strip()
				SENT_TO = DISP_SENT_TO_REGEX.search(content).group().strip()
				SENT_YEARS = DISP_SENT_YEARS_REGEX.search(content).group().strip()
				SENT_MONTHS = DISP_SENT_MONTHS_REGEX.search(content).group().strip()
				SENT_HOURS = DISP_SENT_HOURS_REGEX.search(content).group().strip()
				DATA_DICT['sentence_date'] = clean_val(SENT_DATE)
				DATA_DICT['sentence_by'] = clean_val(SENT_BY)
				DATA_DICT['sentence_to'] = clean_val(SENT_TO)
				DATA_DICT['sentence_years'] = clean_val(SENT_YEARS)
				DATA_DICT['sentence_months'] = clean_val(SENT_MONTHS)
				DATA_DICT['sentence_hours'] = clean_val(SENT_HOURS)
			elif DISP_SENT_BEGIN_REGEX.search(content):
				SENT_BGN = DISP_SENT_BEGIN_REGEX.search(content).group().strip()
				SENT_VOL = DISP_SENT_VOL_REGEX.search(content).group().strip()
				SENT_PAGE = DISP_SENT_PAGE_REGEX.search(content).group().strip()
				DISCH = DISP_DISCHARGE_REGEX.search(content).group().strip()
				DISCH_TYPE = DISP_DISCH_TYPE_REGEX.search(content).group().strip()
				DISP_NUM = DISP_NUM_REGEX.search(content).group().strip()
				DATA_DICT['sentence_to_begin'] = clean_val(SENT_BGN)
				DATA_DICT['sentence_vol'] = clean_val(SENT_VOL)
				DATA_DICT['sentence_page'] = clean_val(SENT_PAGE)
				DATA_DICT['discharge'] = clean_val(DISCH)
				DATA_DICT['discharge_type'] = clean_val(DISCH_TYPE)
				DATA_DICT['discharge_number'] = clean_val(DISP_NUM)
			elif DISP_PROB_SENT_TO_REGEX.search(content):
				PROB_SENT = DISP_PROB_SENT_TO_REGEX.search(content).group().strip()
				PROB_SENT_YEARS = DISP_PROB_SENT_YEARS_REGEX.search(content).group().strip()
				PROB_SENT_MONTHS = DISP_PROB_SENT_MONTHS_REGEX.search(content).group().strip()
				PROB_SENT_DAYS = DISP_PROB_SENT_DAYS_REGEX.search(content).group().strip()
				MULT_SENT = DISP_MULT_SENT_REGEX.search(content).group().strip()
				DATA_DICT['probated_sentence_to'] = clean_val(PROB_SENT)
				DATA_DICT['probation_sentence_years'] = clean_val(PROB_SENT_YEARS)
				DATA_DICT['probation_sentence_months'] = clean_val(PROB_SENT_MONTHS)
				DATA_DICT['probation_sentence_days'] = clean_val(PROB_SENT_DAYS)
				DATA_DICT['mult_sent'] = clean_val(MULT_SENT)
			elif DISP_PROB_YEARS_REGEX.search(content):
				PROB_YEARS = DISP_PROB_YEARS_REGEX.search(content).group().strip()
				PROB_MONTHS = DISP_PROB_MONTHS_REGEX.search(content).group().strip()
				PROB_DAYS = DISP_PROB_DAYS_REGEX.search(content).group().strip()
				PROB_START = DISP_PROB_START_DATE_REGEX.search(content).group().strip()
				DATA_DICT['probated_for_years'] = clean_val(PROB_YEARS)
				DATA_DICT['probated_for_months'] = clean_val(PROB_MONTHS)
				DATA_DICT['probated_for_days'] = clean_val(PROB_DAYS)
				DATA_DICT['probation_start_date'] = clean_val(PROB_START)
			elif DISP_SPEC_COND_1_REGEX.search(content):
				COND_1 = DISP_SPEC_COND_1_REGEX.search(content).group().strip()
				FOR_1 = DISP_FOR_1_REGEX.search(content).group().strip()
				COND_2 = DISP_SPEC_COND_2_REGEX.search(content).group().strip()
				FOR_2 = content[content.rindex('FOR'):].strip('FOR ')
				DATA_DICT['spec_cond_1'] = clean_val(COND_1)
				DATA_DICT['for_1'] = clean_val(FOR_1)
				DATA_DICT['spec_cond_2'] = clean_val(COND_2)
				DATA_DICT['for_2'] = clean_val(FOR_2)
			elif DISP_FINE_CODE_REGEX.search(content):
				FINE_CODE = DISP_FINE_CODE_REGEX.search(content).group().strip()
				FINE_AMT = DISP_FINE_AMT_REGEX.search(content).group().strip()
				COST_CODE = DISP_COST_CODE_REGEX.search(content).group().strip()
				COST_AMT = DISP_COST_AMT_REGEX.search(content).group().strip()
				DUE = DISP_DUE_DATE_REGEX.search(content).group().strip()
				DATA_DICT['fine_code'] = clean_val(FINE_CODE)
				DATA_DICT['fine_amt'] = clean_val(FINE_AMT)
				DATA_DICT['cost_code'] = clean_val(COST_CODE)
				DATA_DICT['cost_amt'] = clean_val(COST_AMT)
				DATA_DICT['payment_due_date'] = clean_val(DUE)
		DATA_LIST.append(DATA_DICT)
		return DATA_LIST

	def get_reduced_enhanced(self, red_enh_trs, da_case_id, jd_case_id):
		red_enh_id = 0
		DATA_LIST = list()
		DATA_DICT = dict()
		for content in red_enh_trs:
			if RED_ENH_DESC_REGEX.search(content):
				if len(DATA_DICT.keys())>0:
					DATA_LIST.append(DATA_DICT)
					DATA_DICT = dict()
				red_enh_id += 1
				DATA_DICT['red_enh_id'] = red_enh_id
				DATA_DICT['da_case_id'] = da_case_id
				DATA_DICT['jd_case_id'] = jd_case_id
				DESC = RED_ENH_DESC_REGEX.search(content).group().strip()
				COMT = RED_ENH_COMT_REGEX.search(content).group().strip()
				TYP_CL = RED_ENH_TYP_CL_REGEX.search(content).group().strip().split()
				GOC = RED_ENH_GOC_REGEX.search(content).group().strip()
				DATA_DICT['desc'] = clean_val(DESC)
				DATA_DICT['comt'] = clean_val(COMT)
				if len(TYP_CL)==2:
					DATA_DICT['typ'] = clean_val(TYP_CL[0]).strip()
					DATA_DICT['cl'] = clean_val(TYP_CL[1]).strip()
				else:
					DATA_DICT['typ'] = clean_val(TYP_CL[0]).strip()
				DATA_DICT['goc'] = clean_val(GOC)
			elif RED_ENH_COUNTY_REGEX.search(content):
				COUNTY = RED_ENH_COUNTY_REGEX.search(content).group().strip()
				STATE = RED_ENH_STATE_REGEX.search(content).group().strip()
				DATA_DICT['county_code'] = clean_val(COUNTY)
				DATA_DICT['state_code'] = clean_val(STATE)
			elif RED_ENH_REVOC_DATE_REGEX.search(content):
				REVOC_FILE = RED_ENH_REVOC_DATE_REGEX.search(content).group().strip()
				WARR_DATE = RED_ENH_WARR_REGEX.search(content).group().strip()
				DATA_DICT['probation_revocation_file_date'] = clean_val(REVOC_FILE)
				DATA_DICT['warrant_issued_date'] = clean_val(WARR_DATE)
			elif RED_ENH_COMMENT_REGEX.search(content):
				COMMENT = RED_ENH_COMMENT_REGEX.search(content).group().strip()
				DATA_DICT['disposition_comment'] = clean_val(COMMENT)
		DATA_LIST.append(DATA_DICT)
		return DATA_LIST

	def get_general_comments(self, comment_trs, da_case_id, jd_case_id):
		comment_id = 0
		DATA_LIST = list()
		DATA_DICT = dict()
		for content in comment_trs:
			if GC_COMMENT_REGEX.search(content):
				if len(DATA_DICT.keys())>0:
					DATA_LIST.append(DATA_DICT)
					DATA_DICT = dict()
				comment_id += 1
				DATA_DICT['comment_id'] = comment_id
				DATA_DICT['da_case_id'] = da_case_id
				DATA_DICT['jd_case_id'] = jd_case_id
				COMMENT = GC_COMMENT_REGEX.search(content).group().strip()
				DATA_DICT['comment'] = clean_val(COMMENT)
			elif GC_DATE_REGEX.search(content):
				DATE = GC_DATE_REGEX.search(content).group().strip()
				DATA_DICT['date'] = clean_val(DATE)
		DATA_LIST.append(DATA_DICT)
		return DATA_LIST

	def get_general_comments_ws(self, comment_ws_trs, da_case_id, jd_case_id):
		comment_id = 0
		DATA_LIST = list()
		DATA_DICT = dict()
		for content in comment_ws_trs:
			if len(DATA_DICT.keys())>0:
				DATA_LIST.append(DATA_DICT)
				DATA_DICT = dict()
			comment_id += 1
			DATA_DICT['comment_id'] = comment_id
			DATA_DICT['da_case_id'] = da_case_id
			DATA_DICT['jd_case_id'] = jd_case_id
			COMMENT = GC_WS_COMMENT_REGEX.search(content).group().strip()
			TYPE = GC_WS_COMMENT_TYPE_REGEX.search(content).group().strip()
			DATE = GC_WS_DATE_REGEX.search(content).group().strip()
			EXTRA = GC_WS_EXTRA_REGEX.search(content).group().strip()
			DATA_DICT['comment'] = clean_val(COMMENT)
			DATA_DICT['comment_type'] = clean_val(TYPE)
			DATA_DICT['comment_date'] = clean_val(DATE)
			DATA_DICT['extra_field'] = clean_val(EXTRA)
		DATA_LIST.append(DATA_DICT)
		return DATA_LIST

	def get_motions(self, motion_trs, da_case_id, jd_case_id):
		motion_id = 0
		DATA_LIST = list()
		DATA_DICT = dict()
		for content in motion_trs:
			if MOT_DISP_NO_REGEX.search(content):
				if len(DATA_DICT.keys())>0:
					DATA_LIST.append(DATA_DICT)
					DATA_DICT = dict()
				motion_id += 1
				DATA_DICT['motion_id'] = motion_id
				DATA_DICT['da_case_id'] = da_case_id
				DATA_DICT['jd_case_id'] = jd_case_id
			elif MOT_FILED_REGEX.search(content):
				FILED = MOT_FILED_REGEX.search(content).group().strip()
				TYPE = MOT_TYPE_REGEX.search(content).group().strip()
				PEND = MOT_PEND_REGEX.search(content).group().strip()
				FACT = MOT_FACTS_REGEX.search(content).group().strip()
				DATA_DICT['motion_filed'] = clean_val(FILED)
				DATA_DICT['motion_type'] = clean_val(TYPE)
				DATA_DICT['motion_pending'] = clean_val(PEND)
				DATA_DICT['statement_of_facts_filed'] = clean_val(FACT)
			elif MOT_DESC_REGEX.search(content):
				DESC = MOT_DESC_REGEX.search(content).group().strip()
				SENT_PEND = MOT_SENT_PEND_REGEX.search(content).group().strip()
				DISP_DT = MOT_DISP_DT_REGEX.search(content).group().strip()
				DISP_TYPE = MOT_DISP_TYPE_REGEX.search(content).group().strip()
				DATA_DICT['desc'] = clean_val(DESC)
				DATA_DICT['sentence_pending'] = clean_val(SENT_PEND)
				DATA_DICT['disposed_date'] = clean_val(DISP_DT)
				DATA_DICT['type'] = clean_val(DISP_TYPE)
			elif MOT_COMMENT_REGEX.search(content):
				COMMENT = MOT_COMMENT_REGEX.search(content).group().strip()
				REC_NO = MOT_REC_NO_REGEX.search(content).group().strip()
				DATA_DICT['comment'] = clean_val(COMMENT)
				DATA_DICT['rec_no'] = clean_val(REC_NO)
		DATA_LIST.append(DATA_DICT)
		return DATA_LIST

	def get_probation_revocation(self, prov_revoc_trs, da_case_id, jd_case_id):
		pr_id = 0
		DATA_LIST = list()
		DATA_DICT = dict()

		for content in prov_revoc_trs:
			if PROB_NO_REGEX.search(content):
				if len(DATA_DICT.keys())>0:
					DATA_LIST.append(DATA_DICT)
					DATA_DICT = dict()
				pr_id += 1
				DISP_NO = PROB_NO_REGEX.search(content).group().strip()
				DATA_DICT['ct_disp_no'] = clean_val(DISP_NO)
				DATA_DICT['da_case_id'] = da_case_id
				DATA_DICT['jd_case_id'] = jd_case_id
			elif PROB_VERDICT_DATE_REGEX.search(content):
				VERDICT_DATE = PROB_VERDICT_DATE_REGEX.search(content).group().strip()
				VERDICT_BY = PROB_VERDICT_BY_REGEX.search(content).group().strip()
				VERDICT_JG = PROB_VERDICT_JG_REGEX.search(content).group().strip()
				TC = PROB_TC_REGEX.search(content).group().strip()
				DISM_TYPE = PROB_DISM_TYP_REGEX.search(content).group().strip()
				VERDICT_VOL = PROB_VERDICT_VOL_REGEX.search(content).group().strip()
				VERDICT_PAGE = PROB_VERDICT_PAGE_REGEX.search(content).group().strip()
				DATA_DICT['verdict_date'] = clean_val(VERDICT_DATE)
				DATA_DICT['verdict_by'] = clean_val(VERDICT_BY)
				DATA_DICT['verdict_jg'] = clean_val(VERDICT_JG)
				DATA_DICT['verdict_tc'] = clean_val(TC)
				DATA_DICT['dism_type'] = clean_val(DISM_TYPE)
				DATA_DICT['verdict_vol'] = clean_val(VERDICT_VOL)
				DATA_DICT['verdict_page'] = clean_val(VERDICT_PAGE)
			elif PROB_SENT_DATE_REGEX.search(content):
				SENT_DATE = PROB_SENT_DATE_REGEX.search(content).group().strip()
				SENT_BY = PROB_SENT_BY_REGEX.search(content).group().strip()
				SENT_TO = PROB_SENT_TO_REGEX.search(content).group().strip()
				SENT_YEARS = PROB_SENT_YEARS_REGEX.search(content).group().strip()
				SENT_MONTHS = PROB_SENT_MONTHS_REGEX.search(content).group().strip()
				SENT_DAYS = PROB_SENT_DAYS_REGEX.search(content).group().strip()
				SENT_HOURS = PROB_SENT_HOURS_REGEX.search(content).group().strip()
				DATA_DICT['sentence_date'] = clean_val(SENT_DATE)
				DATA_DICT['sentence_by'] = clean_val(SENT_BY)
				DATA_DICT['sentence_to'] = clean_val(SENT_TO)
				DATA_DICT['sentence_years'] = clean_val(SENT_YEARS)
				DATA_DICT['sentence_months'] = clean_val(SENT_MONTHS)
				DATA_DICT['sentence_days'] = clean_val(SENT_DAYS)
				DATA_DICT['sentence_hours'] = clean_val(SENT_HOURS)
			elif PROB_SENT_BEGIN_REGEX.search(content):
				SENT_BGN = PROB_SENT_BEGIN_REGEX.search(content).group().strip()
				SENT_VOL = PROB_SENT_VOL_REGEX.search(content).group().strip()
				SENT_PAGE = PROB_SENT_PAGE_REGEX.search(content).group().strip()
				DISCH = PROB_DISCHARGE_REGEX.search(content).group().strip()
				DISCH_TYPE = PROB_DISCH_TYPE_REGEX.search(content).group().strip()
				DISP_NUM = PROB_NUM_REGEX.search(content).group().strip()
				DATA_DICT['sentence_to_begin'] = clean_val(SENT_BGN)
				DATA_DICT['sentence_vol'] = clean_val(SENT_VOL)
				DATA_DICT['sentence_page'] = clean_val(SENT_PAGE)
				DATA_DICT['discharge'] = clean_val(DISCH)
				DATA_DICT['discharge_type'] = clean_val(DISCH_TYPE)
				DATA_DICT['discharge_number'] = clean_val(DISP_NUM)
			elif PROB_PROB_SENT_TO_REGEX.search(content):
				PROB_SENT = PROB_PROB_SENT_TO_REGEX.search(content).group().strip()
				PROB_SENT_YEARS = PROB_PROB_SENT_YEARS_REGEX.search(content).group().strip()
				PROB_SENT_MONTHS = PROB_PROB_SENT_MONTHS_REGEX.search(content).group().strip()
				PROB_SENT_DAYS = PROB_PROB_SENT_DAYS_REGEX.search(content).group().strip()
				MULT_SENT = PROB_MULT_SENT_REGEX.search(content).group().strip()
				DATA_DICT['probated_sentence_to'] = clean_val(PROB_SENT)
				DATA_DICT['probation_sentence_years'] = clean_val(PROB_SENT_YEARS)
				DATA_DICT['probation_sentence_months'] = clean_val(PROB_SENT_MONTHS)
				DATA_DICT['probation_sentence_days'] = clean_val(PROB_SENT_DAYS)
				DATA_DICT['mult_sent'] = clean_val(MULT_SENT)
			elif PROB_PROB_YEARS_REGEX.search(content):
				PROB_YEARS = PROB_PROB_YEARS_REGEX.search(content).group().strip()
				PROB_MONTHS = PROB_PROB_MONTHS_REGEX.search(content).group().strip()
				PROB_DAYS = PROB_PROB_DAYS_REGEX.search(content).group().strip()
				PROB_START = PROB_PROB_START_DATE_REGEX.search(content).group().strip()
				DATA_DICT['probated_for_years'] = clean_val(PROB_YEARS)
				DATA_DICT['probated_for_months'] = clean_val(PROB_MONTHS)
				DATA_DICT['probated_for_days'] = clean_val(PROB_DAYS)
				DATA_DICT['probation_start_date'] = clean_val(PROB_START)
			elif PROB_SPEC_COND_1_REGEX.search(content):
				COND_1 = PROB_SPEC_COND_1_REGEX.search(content).group().strip()
				FOR_1 = PROB_FOR_1_REGEX.search(content).group().strip()
				COND_2 = PROB_SPEC_COND_2_REGEX.search(content).group().strip()
				FOR_2 = content[content.rindex('FOR'):].strip('FOR ')
				DATA_DICT['spec_cond_1'] = clean_val(COND_1)
				DATA_DICT['for_1'] = clean_val(FOR_1)
				DATA_DICT['spec_cond_2'] = clean_val(COND_2)
				DATA_DICT['for_2'] = clean_val(FOR_2)
			elif PROB_FINE_CODE_REGEX.search(content):
				FINE_CODE = PROB_FINE_CODE_REGEX.search(content).group().strip()
				FINE_AMT = PROB_FINE_AMT_REGEX.search(content).group().strip()
				COST_CODE = PROB_COST_CODE_REGEX.search(content).group().strip()
				COST_AMT = PROB_COST_AMT_REGEX.search(content).group().strip()
				DUE = PROB_DUE_DATE_REGEX.search(content).group().strip()
				DATA_DICT['fine_code'] = clean_val(FINE_CODE)
				DATA_DICT['fine_amt'] = clean_val(FINE_AMT)
				DATA_DICT['cost_code'] = clean_val(COST_CODE)
				DATA_DICT['cost_amt'] = clean_val(COST_AMT)
				DATA_DICT['payment_due_date'] = clean_val(DUE)
		DATA_LIST.append(DATA_DICT)
		return DATA_LIST

	def get_appeals(self, appeal_trs, da_case_id, jd_case_id):
		appeal_id = 0
		DATA_LIST = list()
		DATA_DICT = dict()

		for content in appeal_trs:
			if APPL_NO_REGEX.search(content):
				if len(DATA_DICT.keys())>0:
					DATA_LIST.append(DATA_DICT)
					DATA_DICT = dict()
				appeal_id += 1
				DATA_DICT['appeal_id'] = appeal_id
				DATA_DICT['da_case_id'] = da_case_id
				DATA_DICT['jd_case_id'] = jd_case_id
				CT_DISP_NO = APPL_NO_REGEX.search(content).group().strip()
				DATA_DICT['ct_disp_no'] = clean_val(CT_DISP_NO)
			elif APPL_DATE_REGEX.search(content):
				DATE_MADE = APPL_DATE_REGEX.search(content).group().strip()
				FACT_FILE = APPL_FILE_REGEX.search(content).group().strip()
				EXT = APPL_EXT_REGEX.search(content).group().strip()
				DATA_DICT['date_appeal_made'] = clean_val(DATE_MADE)
				DATA_DICT['copy_statement_of_facts_filed'] = clean_val(FACT_FILE)
				DATA_DICT['extended'] = clean_val(EXT)
			elif APPL_DESIG_REGEX.search(content):
				DESIG = APPL_DESIG_REGEX.search(content).group().strip()
				STATE = APPL_STATE_REGEX.search(content).group().strip()
				TRANS = APPL_TRANS_REGEX.search(content).group().strip()
				DATA_DICT['designation_of_record_defense'] = clean_val(DESIG)
				DATA_DICT['state'] = clean_val(STATE)
				DATA_DICT['transcript_filed'] = clean_val(TRANS)
			elif APPL_OBJ_REGEX.search(content):
				OBJ = APPL_OBJ_REGEX.search(content).group().strip()
				NOTICE = APPL_NOT_REGEX.search(content).group().strip()
				DATA_DICT['objection'] = clean_val(OBJ)
				DATA_DICT['date_notice_sent'] = clean_val(NOTICE)
			elif APPL_DATE_SENT_REGEX.search(content):
				DATE_SENT = APPL_DATE_SENT_REGEX.search(content).group().strip()
				OPINION = APPL_OPINION_REGEX.search(content).group().strip()
				MAND_REC = APPL_MAND_REC_REGEX.search(content).group().strip()
				DISP = APPL_DISP_REGEX.search(content).group().strip()
				DATA_DICT['date_sent_to_appeals'] = clean_val(DATE_SENT)
				DATA_DICT['opinion_date'] = clean_val(OPINION)
				DATA_DICT['mandate_received'] = clean_val(MAND_REC)
				DATA_DICT['disp'] = clean_val(DISP)
			elif APPL_MAND_ENF_REGEX.search(content):
				MAND_ENF = APPL_MAND_ENF_REGEX.search(content).group().strip()
				WITHDRAW = APPL_WITH_REGEX.search(content).group().strip()
				REPORTER = APPL_REPORTER_REGEX.search(content).group().strip()
				DATA_DICT['mandate_enforced_date'] = clean_val(MAND_ENF)
				DATA_DICT['appeal_withdrawn'] = clean_val(WITHDRAW)
				DATA_DICT['ct_reporter_initials'] = clean_val(REPORTER)
			elif APPL_REF_CODE_REGEX.search(content):
				REF_CODE = APPL_REF_CODE_REGEX.search(content).group().strip()
				REC_NO = APPL_REC_NO_REGEX.search(content).group().strip()
				DATA_DICT['appeal_ref_code'] = clean_val(REF_CODE)
				DATA_DICT['rec_no'] = clean_val(REC_NO)
		DATA_LIST.append(DATA_DICT)
		return DATA_LIST

	def get_competency_data(self, comp_trs, da_case_id, jd_case_id):
		comp_id = 0
		DATA_LIST = list()
		DATA_DICT = dict()

		for content in comp_trs:
			if COMP_DATE_REGEX.search(content):
				if len(DATA_DICT.keys())>0:
					DATA_LIST.append(DATA_DICT)
					DATA_DICT = dict()
				comp_id += 1
				DATA_DICT['competency_id'] = comp_id
				DATA_DICT['da_case_id'] = da_case_id
				DATA_DICT['jd_case_id'] = jd_case_id
				DATE = COMP_DATE_REGEX.search(content).group().strip()
				PURP = COMP_PURP_REGEX.search(content).group().strip()
				RES = COMP_RESULT_REGEX.search(content).group().strip()
				FIND = COMP_FIND_REGEX.search(content).group().strip()
				DATA_DICT['hearing_date'] = clean_val(DATE)
				DATA_DICT['purpose'] = clean_val(PURP)
				DATA_DICT['result'] = clean_val(RES)
				DATA_DICT['finding_by'] = clean_val(FIND)
			elif COMP_COMMENT_REGEX.search(content):
				COMMENT = COMP_COMMENT_REGEX.search(content).group().strip()
				REC_NO = COMP_REC_NO_REGEX.search(content).group().strip()
				DATA_DICT['comment'] = clean_val(COMMENT)
				DATA_DICT['rec_no'] = clean_val(REC_NO)
		DATA_LIST.append(DATA_DICT)
		return DATA_LIST

	def get_payments(self, payment_trs, da_case_id, jd_case_id):
		payment_id = 0
		DATA_LIST = list()
		DATA_DICT = dict()

		for content in payment_trs:
			if PAY_DISP_NO_REGEX.search(content):
				if len(DATA_DICT.keys())>0:
					DATA_LIST.append(DATA_DICT)
					DATA_DICT = dict()
				payment_id += 1
				DATA_DICT['payment_id'] = payment_id
				DATA_DICT['da_case_id'] = da_case_id
				DATA_DICT['jd_case_id'] = jd_case_id
				DISP_NO = PAY_DISP_NO_REGEX.search(content).group().strip()
				DATA_DICT['ct_disp_no'] = clean_val(DISP_NO)
			elif PAY_DATE_REGEX.search(content):
				DATE_PAID = PAY_DATE_REGEX.search(content).group().strip()
				AMT_PAID = PAY_AMT_REGEX.search(content).group().strip()
				TYPE_PAYMENT = PAY_TYPE_REGEX.search(content).group().strip()
				RECEIPT_NO = PAY_RECEIPT_REGEX.search(content).group().strip()
				DATA_DICT['date_paid'] = clean_val(DATE_PAID)
				DATA_DICT['amt_paid'] = clean_val(AMT_PAID)
				DATA_DICT['type_payment'] = clean_val(TYPE_PAYMENT)
				DATA_DICT['receipt_no'] = clean_val(RECEIPT_NO)
			elif PAY_RECD_BY_REGEX.search(content):
				RECD_BY = PAY_RECD_BY_REGEX.search(content).group().strip()
				PD_UP = PAY_PD_UP_REGEX.search(content).group().strip()
				NEXT_DT = PAY_NEXT_DT_REGEX.search(content).group().strip()
				NEXT_AMT = PAY_NEXT_AMT_REGEX.search(content).group().strip()
				DATA_DICT['received_by'] = clean_val(RECD_BY)
				DATA_DICT['pd_up'] = clean_val(PD_UP)
				DATA_DICT['date_next_payment'] = clean_val(NEXT_DT)
				DATA_DICT['amt_next_payment'] = clean_val(NEXT_AMT)
			elif PAY_REC_NO_REGEX.search(content):
				REC_NO = PAY_REC_NO_REGEX.search(content).group().strip()
				DATA_DICT['rec_no'] = clean_val(REC_NO)
		DATA_LIST.append(DATA_DICT)
		return DATA_LIST

	def get_bond_comments(self, bond_comment_trs, da_case_id, jd_case_id):
		comment_id = 0
		DATA_LIST = list()
		DATA_DICT = dict()

		for content in BOND_COMMENT_TRS:
			if BC_DATE_REGEX.search(content):
				if len(DATA_DICT.keys())>0:
					DATA_LIST.append(DATA_DICT)
					DATA_DICT = dict()
				comment_id += 1
				DATA_DICT['comment_id'] = comment_id
				DATA_DICT['da_case_id'] = da_case_id
				DATA_DICT['jd_case_id'] = jd_case_id
				DATE = BC_DATE_REGEX.search(content).group().strip()
				DATA_DICT['date'] = clean_val(DATE)
			elif BC_COMMENT_REGEX.search(content):
				COMMENT = BC_COMMENT_REGEX.search(content).group().strip()
				FUNC = BC_FUNC_REGEX.search(content).group().strip()
				DATA_DICT['comment'] = clean_val(COMMENT)
				DATA_DICT['func'] = clean_val(FUNC)
		DATA_LIST.append(DATA_DICT)
		return DATA_LIST

	def parse(self, html_fn):
		EXPORT_DATA = dict()
		html_fp = os.path.join(self.input_path, html_fn)
		html = ''
		with open(html_fp, 'r') as inp:
			html = inp.read()
		soup_res = BeautifulSoup(html.encode('iso-8859-1'), 'lxml')

		table = soup_res.find('table', attrs={'class':'table'})
		trs = [tr for tr in table.find_all('tr') if len(tr.text.strip())>0
				and FILTER_REGEX.search(tr.text.strip()) is None]

		last_updated_raw = table.find_all('td')[-1].text.strip()
		last_updated = str(parse(last_updated_raw, tzinfos=TZ_INFOS))

		case_ids = unicodedata.normalize('NFKD', [tr for tr in table.find_all('tr') if tr.text.strip().startswith('¢')][0].text.strip())
		try:
			DA_CASE_ID = DA_CASE_ID_REGEX.search(case_ids).group().strip()
		except:
			DA_CASE_ID = ''
		try:
			JD_CASE_ID = JD_CASE_ID_REGEX.search(case_ids).group().strip()
		except:
			JD_CASE_ID = ''

		JUDICIAL_TRS, SETS_TRS, NAMES_TRS, BONDS_TRS, CHARGE_TRS, \
			DISP_TRS, RED_ENH_TRS, COMMENT_TRS, COMMENT_WS_TRS, \
			MOTION_TRS, PROB_REVOC_TRS, APPEAL_TRS, COMP_TRS, \
			PAYMENT_TRS, BOND_COMMENT_TRS = self.extract_tables(trs)

		if len(JUDICIAL_TRS)>0:
			EXPORT_DATA['judicial_information'] = self.get_judicial_information(JUDICIAL_TRS, DA_CASE_ID, JD_CASE_ID)
		if len(SETS_TRS)>0:
			EXPORT_DATA['sets_and_passes'] = self.get_sets_and_passes(SETS_TRS, DA_CASE_ID, JD_CASE_ID)
		if len(NAMES_TRS)>0:
			EXPORT_DATA['names'] = self.get_names(NAMES_TRS, DA_CASE_ID, JD_CASE_ID)
		if len(BONDS_TRS)>0:
			EXPORT_DATA['bonds'] = self.get_bonds(BONDS_TRS, DA_CASE_ID, JD_CASE_ID)
		if len(CHARGE_TRS)>0:
			EXPORT_DATA['charges'] = self.get_charges(CHARGE_TRS, DA_CASE_ID, JD_CASE_ID)
		if len(DISP_TRS)>0:
			EXPORT_DATA['dispositions'] = self.get_dispositions(DISP_TRS, DA_CASE_ID, JD_CASE_ID)
		if len(RED_ENH_TRS)>0:
			EXPORT_DATA['reduced_enhanced_charges'] = self.get_reduced_enhanced(RED_ENH_TRS, DA_CASE_ID, JD_CASE_ID)
		if len(COMMENT_TRS)>0:
			EXPORT_DATA['general_comments'] = self.get_general_comments(COMMENT_TRS, DA_CASE_ID, JD_CASE_ID)
		if len(COMMENT_WS_TRS)>0:
			EXPORT_DATA['general_comments_ws_date'] = self.get_general_comments_ws(COMMENT_WS_TRS, DA_CASE_ID, JD_CASE_ID)
		if len(MOTION_TRS)>0:
			EXPORT_DATA['motions'] = self.get_motions(MOTION_TRS, DA_CASE_ID, JD_CASE_ID)
		if len(PROB_REVOC_TRS)>0:
			EXPORT_DATA['probation_revocation'] = self.get_probation_revocation(PROB_REVOC_TRS, DA_CASE_ID, JD_CASE_ID)
		if len(APPEAL_TRS)>0:
			EXPORT_DATA['appeals'] = self.get_appeals(APPEAL_TRS, DA_CASE_ID, JD_CASE_ID)
		if len(COMP_TRS)>0:
			EXPORT_DATA['competency_data'] = self.get_competency_data(COMP_TRS, DA_CASE_ID, JD_CASE_ID)
		if len(PAYMENT_TRS)>0:
			EXPORT_DATA['payments'] = self.get_payments(PAYMENT_TRS, DA_CASE_ID, JD_CASE_ID)
		if len(BOND_COMMENT_TRS)>0:
			EXPORT_DATA['bond_comments'] = self.get_bond_comments(BOND_COMMENT_TRS, DA_CASE_ID, JD_CASE_ID)

		return (EXPORT_DATA, last_updated)

	def run(self):
		for html_fn in tqdm([fn for fn in os.listdir(self.input_path) if fn.endswith('.html')]):
			EXPORT_DATA, last_updated = self.parse(html_fn)
			for key in EXPORT_DATA.keys():
				column_list = TXDallasParser.COLUMN_ORDER[key]
				data = EXPORT_DATA[key]
				if type(data)==dict:
					data = [data]
				[d.update({'last_updated':last_updated}) for d in data]
				df = pd.DataFrame(data, columns=column_list)
				outfile = os.path.join(self.output_path, '{}.xlsx'.format(key))
				if not os.path.exists(outfile):
					with pd.ExcelWriter(outfile, engine='openpyxl', mode='w') as writer:
						df.to_excel(writer, index=False, header=True)
				else:
					wb = load_workbook(outfile)
					sheet = wb.active
					row_data = list()
					for d in data:
						row_data.append([d[k] if k in d.keys() else '' for k in column_list])
					for row in row_data:
						sheet.append(row)
					wb.save(outfile)
