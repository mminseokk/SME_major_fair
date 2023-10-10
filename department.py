def department(department_df, physics_user, code_user, team_user, optimization_user):
    min_mse = float('inf') * (1)
    department = None 
    for df in department_df:
            mse_sum = (physics_user - df['physics'])**2 + (code_user - df['code'])**2 +(team_user - df['team'])**2 + (optimization_user - df['optimization'])**2 
            if mse_sum < min_mse:
                min_mse = mse_sum   
                department = df['department']
                
    return department