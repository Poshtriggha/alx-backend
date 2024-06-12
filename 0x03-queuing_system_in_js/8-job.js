function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw Error('Jobs is not an array');
    }

    jobs.forEach((jobdata) => {
        let job = queue.create('push_notification_code_3', jobdata);

        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        }).on('failed', (err) => {
            console.error(`Notification job ${job.id} failed: ERROR`)
        }).on('progress', (progress) => {
            console.log(`Notification job ${job.id} PERCENT% complete`)
        });
        job.save((error) => {
            if (!error) console.log(`Notification job created: ${job.id}`);
        });
    });
}

module.exports = createPushNotificationsJobs;