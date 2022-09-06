from jenkinsapi.jenkins import Jenkins

myUrl = "http://localhost:8080/"
myUsername = "vila274183"
myPassword = "110a3997288372c6645b6bb24676bf4ad7"

jnk = Jenkins(myUrl, myUsername, myPassword)
totalBuildCount = 0

for jobs in jnk.keys():
    builds = jnk[jobs].get_build_dict()
    print (jobs + " = build count: " + str(len(builds)))
    # totalBuildCount += len(builds)
    #print (jobs)
    #jnk.build_job(jobs,'')

# print ("Total build count: " + str(totalBuildCount))
job = "test"
jnk.build_job(job)
