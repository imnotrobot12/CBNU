# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 15:19:26 2021

@author: JiHyeunKim
"""
from durable.lang import *

#Pouch Battery Inspection
with ruleset('PBI') :
    @when_all(+m.object)
    def out(c) :
        print( 'Fact : {0}의 {1}이/가 {2}이다.'.format(c.m.Subject, c.m.object, c.m.Result))
        
    @when_all(m.Prepare != 'Success')
    def A(c):
        if c.m.Subject == 'Vision' :
            print('Input Fact : {0}의 Prepare이/가 {1}이다.'.format(c.m.Subject, c.m.Prepare))
            c.assert_fact({'Subject' : c.m.Subject, 'object' : 'Hardware' , 'Result' : 'Bad'})
                    
    @when_all( (m.object == 'Hardware') & (m.Result == 'Bad') )
    def B(c) :
        print('Solution : {0} 연결상태를 체크하세요.\n'.format(c.m.object))
        
    @when_all( m.AI == 'Good')
    def C(c):
        c.assert_fact({'Subject' : c.m.Subject, 'object' : 'HostResult' , 'Result' : 'OK'})
    
    @when_all( m.AI == 'Bad')
    def F(c):
        c.assert_fact({'Subject' : c.m.Subject, 'object' : 'HostResult' , 'Result' : 'NG'})
        
    @when_all( (m.RBS == 'Good') & (m.AI == 'Good'))
    def D(c) :
        c.assert_fact({'Subject' : c.m.Subject, 'object' : 'Vision Insp' , 'Result' : 'Good'})
        
    @when_all( (m.RBS == 'Good') & (m.AI == 'Bad'))
    def E(c) :
        c.assert_fact({'Subject' : c.m.Subject, 'object' : 'Vision Insp' , 'Result' : 'Bad'})
        
    @when_all( (m.RBS == 'Bad') & (m.AI == 'Bad'))
    def G(c) :
        c.assert_fact({'Subject' : c.m.Subject, 'object' : 'Vision Insp' , 'Result' : 'Good'})
        
    @when_all( (m.RBS == 'Bad') & (m.AI == 'Good'))
    def H(c) :
        c.assert_fact({'Subject' : c.m.Subject, 'object' : 'Vision Insp' , 'Result' : 'Bad'})
   
    @when_all( (m.Result == 'Unmatch') )
    def L(c) :
        print( 'Solution : {0}의 {1}을/를 체크하세요.\n'.format(c.m.Subject, c.m.object))
        
    @when_all( (m.Subject == 'DeepLearning') & (m.Prepare == 'Fail'))
    def  I(c) :
        print('Input Fact : {0}의 Prepare/가 {1}이다.'.format(c.m.Subject, c.m.Prepare))
        c.assert_fact({'Subject' : c.m.Subject, 'object' : 'Workspace' , 'Result' : 'Unmatch'})
        
        
    @when_all( m.object == 'Workspace')
    def  J(c) :
        c.assert_fact({'Subject' : c.m.Subject, 'object' : 'Stream' , 'Result' : 'Unmatch'})
        
    @when_all( m.object == 'Stream')
    def  K(c) :
        c.assert_fact({'Subject' : c.m.Subject, 'object' : 'Tool' , 'Result' : 'Unmatch'})
    
      
    @when_all( (m.Prepare == 'Success') & (m.RBS == 'Invalid') )
    def M(c) :
        print('Input Fact : {0}의 Prepare가 {1}이지만 RBS가 {2}이다.'.format(c.m.Subject, c.m.Prepare, c.m.RBS))
        c.assert_fact({'Subject' : c.m.Subject, 'object' : 'Align' , 'Result' : 'NG'})
        
    @when_all( (m.object == 'Align') & (m.Result == 'NG') )
    def N(c) :
        print('Solution : {0} Parameter을/를 수정하세요.\n'.format(c.m.object))

        
assert_fact('PBI', {'Subject' : 'Vision', 'Prepare' : 'Fail'})
assert_fact('PBI', {'Subject' : 'DeepLearning', 'Prepare' : 'Fail'})
assert_fact('PBI', {'Subject' : 'Vision', 'Prepare' : 'Success', 'RBS' : 'Invalid'})
assert_fact('PBI', {'Subject' : 'Vision2', 'Prepare' : 'Success', 'RBS' : 'Good', 'AI' : 'Good'})
assert_fact('PBI', {'Subject' : 'Vision3', 'Prepare' : 'Success', 'RBS' : 'Good', 'AI' : 'Bad'})
assert_fact('PBI', {'Subject' : 'Vision5', 'Prepare' : 'Success', 'RBS' : 'Bad', 'AI' : 'Good'})
assert_fact('PBI', {'Subject' : 'Vision6', 'Prepare' : 'Success', 'RBS' : 'Bad', 'AI' : 'Bad'})


