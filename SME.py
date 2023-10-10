def department_text(username, selected_department):
    text = None
    if selected_department == '시스템경영공학과':
        text = f"{username} 님이 선택한 결과를 분석했을 때, 시스템경영공학과이 어울리는 학생입니다." + "\n" + f"시스템경영공학과 학생회 원스미 일동은 {username} 님이 꼭 시스템경영공학과에 전공 진입하셔서, 내년 학과 활동에서 뵙기를 바랍니다😀 궁금한 사항이 있다면 부담갖지 마시고 학생회에게 물어보세요! 다른 학과 부스도 방문해보세요 ✋🏻" 
    else:
        text = f"{username} 님이 선택한 결과를 분석했을 때, {selected_department}가 어울리는 학생입니다." + "\n" + "하지만 최적화, 품질관리, 데이터과학, 인공지능, 스마트팩토리, 인간공학을 배우는 시스템경영공학과에도 관심을 가져주시길 바랍니다😀 궁금한 사항이 있다면 부담갖지 마시고 학생회에게 물어보세요! 다른 학과 부스도 방문해보세요 ✋🏻" 
    return text 