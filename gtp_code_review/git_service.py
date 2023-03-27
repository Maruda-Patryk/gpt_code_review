import git


class GitService:
    def __init__(self, repo_path='.', main_branch='master', review_branch=None):
        self.repo = git.Repo(repo_path)

        self.main_branch = self.repo.branches[main_branch]
        self.review_branch = self.repo.branches[review_branch] if review_branch else self.repo.active_branch
        self.diffs = self.get_diff()

    def get_diff(self):
        return self.main_branch.commit.diff(self.review_branch.commit)

    def get_diffs_content_separated_by_file(self):
        diffs_content = {}
        for diff in self.diffs:
            if diff.new_file:
                diffs_content[diff.b_path] = diff.b_blob.data_stream.read().decode('utf-8')
            elif diff.deleted_file:
                pass
            else:
                diffs_content[diff.b_path] = diff.diff.decode('utf-8')

        return diffs_content

