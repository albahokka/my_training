def components_sandwich(*components):
    print('\nComponents in ur sandwich:')
    for component in components:
        print(f'- {component.title()}')

components_sandwich('tuna', 'mushrooms', 'cheese')
components_sandwich('mushrooms')
components_sandwich('cheese', 'mushrooms')