#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module offers general convenience and utility functions for dealing with parsed data.
"""
from __future__ import unicode_literals
import re

TZ_INFOS = {
	'CDT': 'UTC-5',
}

JUDICIAL_HEADERS = [
	'da_case_id', 'jd_case_id',
	'name_raw',
	'race', 'sex', 'dob', 'age',
	'def_adr1', 'ac', 'ph', 'ss',
	'city', 'state', 'zip', 'dl_number', 'dl_state',
	'offense', 'offense_date', 'offense_type', 'offense_class',
	'goc', 'cat', 'offense_code',
	'comt', 'sid_number', 'of_amt',
	'complainant', 'tape_number', 'arrest_date',
	'juvenile_status', 'repeat_offender', 'career_offender', 'orig_loc', 'curr_loc',
	'filing_agency', 'ser_cas_number', 'arrest_number',
	'lai_number', 'ais_dso_number', 'booking_number',
	'jp_file_date', 'jp_case_id', 'jp_court_id', 'fed', 'evh', 'aff',
	'magistrate_date', 'magis_court', 'magis_judge', 'bound_over',
	'exam_trial_date', 'exam_court', 'exam_judge', 'ind_meth',
	'gj_h_r_date', 'gj_number', 'gj_w_file', 'gj_ds', 'da_dsp', 'acc', 'reas',
	'da_dispos_date', 'misdemeanor_reduction', 'sentence_probated',
	'judcl_case_id', 'gj_ct', 'pros_stat', 'pros_name',
	'court_assigned_to', 'date_assigned', 'assigned_by', 'reason',
	'preceeding_da_case_id', 'succeeding_da_case_id',
	'trn', 'trs', 'warrant_status', 'state_offense_code',
	'last_updated'
]

SETS_HEADERS = [
	'da_case_id', 'jd_case_id',
	'sp_id', 'set_for_date', 'set_for_time', 'set_type', 'passed_to_date',
	'set_disposition_code', 'passed_generally', 'comments',
	'states_recommendation', 'rec_no',
	'last_updated'
]

NAMES_HEADERS = [
	'da_case_id', 'jd_case_id',
	'name_id', 'associated_name', 'name_ref_code',
	'ct_appointed', 'bar_no', 'bond_maker', 'dt_bond_made',
	'last_updated'
]

BONDS_HEADERS = [
	'da_case_id', 'jd_case_id',
	'bond_id', 'date_bond_set',
	'amt', 'type', 'set_by_court',
	'judge', 'rec_no',
	'last_updated'
]

CHARGES_HEADERS = [
	'da_case_id', 'jd_case_id',
	'charge_id', 'name_raw', 'offense_cd', 'state_cd',
	'offense_desc', 'comt', 'offense_type', 'offense_class',
	'goc', 'gj_court', 'current_court', 'previous_courts', 'chov_dt',
	'last_updated'
]

DISPOSITIONS_HEADERS = [
	'da_case_id', 'jd_case_id', 'disp_id', 'ct_disp_no',
	'verdict_date', 'verdict_by', 'verdict_jg', 'verdict_tc',
	'dism_type', 'verdict_vol', 'verdict_page',
	'sentence_date', 'sentence_by', 'sentence_to',
	'sentence_years', 'sentence_months', 'sentence_hours',
	'sentence_to_begin', 'sentence_vol', 'sentence_page',
	'discharge', 'discharge_type', 'discharge_number',
	'probated_sentence_to', 'probation_sentence_years',
	'probation_sentence_months', 'probation_sentence_days',
	'mult_sent', 'probated_for_years', 'probated_for_months',
	'probated_for_days', 'probation_start_date',
	'spec_cond_1', 'for_1', 'spec_cond_2', 'for_2',
	'fine_code', 'fine_amt', 'cost_code', 'cost_amt',
	'payment_due_date',
	'last_updated'
]

RED_ENH_HEADERS = [
	'da_case_id', 'jd_case_id', 'red_enh_id',
	'desc', 'comt', 'typ', 'cl',
	'goc', 'county_code', 'state_code',
	'probation_revocation_file_date',
	'warrant_issued_date', 'disposition_comment',
	'last_updated'
]

GC_HEADERS = [
	'da_case_id', 'jd_case_id', 'comment_id',
	'comment', 'date',
	'last_updated'
]

GC_WS_DATE_HEADERS = [
	'da_case_id', 'jd_case_id', 'comment_id',
	'comment', 'comment_type', 'comment_date', 'extra_field',
	'last_updated'
]

MOTIONS_HEADERS = [
	'da_case_id', 'jd_case_id', 'motion_id',
	'motion_filed', 'motion_type', 'motion_pending', 'statement_of_facts_filed',
	'desc', 'sentence_pending', 'disposed_date', 'type',
	'comment', 'rec_no',
	'last_updated'
]

PROB_REVOC_HEADERS = [
	'da_case_id', 'jd_case_id', 'ct_disp_no',
	'verdict_date', 'verdict_by', 'verdict_jg', 'verdict_tc',
	'dism_type', 'verdict_vol', 'verdict_page',
	'sentence_date', 'sentence_by', 'sentence_to',
	'sentence_years', 'sentence_months', 'sentence_days', 'sentence_hours',
	'sentence_to_begin', 'sentence_vol', 'sentence_page',
	'discharge', 'discharge_type', 'discharge_number',
	'probated_sentence_to', 'probation_sentence_years',
	'probation_sentence_months', 'probation_sentence_days',
	'mult_sent', 'probated_for_years', 'probated_for_months',
	'probated_for_days', 'probation_start_date',
	'spec_cond_1', 'for_1', 'spec_cond_2', 'for_2',
	'fine_code', 'fine_amt', 'cost_code', 'cost_amt', 'payment_due_date',
	'last_updated'
]

APPEALS_HEADERS = [
	'da_case_id', 'jd_case_id', 'appeal_id', 'ct_disp_no',
	'date_appeal_made', 'copy_statement_of_facts_filed', 'extended',
	'designation_of_record_defense', 'state', 'transcript_filed',
	'objection', 'date_notice_sent',
	'date_sent_to_appeals', 'opinion_date', 'mandate_received', 'disp',
	'mandate_enforced_date', 'appeal_withdrawn', 'ct_reporter_initials',
	'appeal_ref_code', 'rec_no',
	'last_updated'
]

COMPETENCY_HEADERS = [
	'da_case_id', 'jd_case_id', 'competency_id',
	'hearing_date', 'purpose', 'result', 'finding_by',
	'comment', 'rec_no',
	'last_updated'
]

PAYMENTS_HEADERS = [
	'da_case_id', 'jd_case_id', 'payment_id', 'ct_disp_no',
	'date_paid', 'amt_paid', 'type_payment', 'receipt_no',
	'received_by', 'pd_up', 'date_next_payment',
	'amt_next_payment', 'rec_no',
	'last_updated'
]

BOND_COMMENTS_HEADERS = [
	'da_case_id', 'jd_case_id', 'comment_id', 'date',
	'comment', 'func',
	'last_updated'
]

def clean_val(val):
	"""
	Returns cleaned value after replacing underscores (`'_'`) and asterisks (`'*'`) with
	an empty whitespace.

	:param val:
		Raw parsed string

	:return:
		A :py:class:`str` object after removing underscores and asterisks
	"""
	return re.sub(r'[_*]', ' ', val).strip()
