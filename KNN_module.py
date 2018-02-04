# K Nearest Neighbors
parameters = {'n_neighbors': np.arange(1, 22, 4)}
clf = GridSearchCV(KNeighborsClassifier(), parameters) #implements a “fit” and a “score” method

clf.fit(Xtest,Ytest)
estm = pd.DataFrame.from_dict(clf.cv_results_)

x, y = clf.best_params_['n_neighbors'], clf.best_score_
text = 'N Neighbors = {}, Score = {}'.format(x, y)

plt.figure()
plt.title('K Nearest Neighbors')
plt.xlabel('Number. of Neighbors')
plt.ylabel('Accuracy Score')
plt.yticks(np.arange(0.6, 0.81, 0.02))

plt.plot(estm.param_n_neighbors, estm.mean_test_score, label='Mean Accuracy Score')
plt.plot(x, y, 'o', label=text)

plt.legend()

	