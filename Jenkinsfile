properties([pipelineTriggers([pollSCM(ignorePostCommitHooks: true, scmpoll_spec: '* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/ShirNeulaender/DevOps3006.git"
    }
    stage("show files"){
        bat "dir"
    }
}
