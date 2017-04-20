%global archive_name ansible-lint
%global lib_name ansiblelint

Name:           %{archive_name}
Version:        3.4.12
Release:        1%{?dist}
Summary:        Best practices checker for Ansible

License:        MIT
URL:            https://github.com/willthames/ansible-lint
Source0:        https://github.com/willthames/%{archive_name}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  ansible
Requires:       ansible

%description
Checks playbooks for practices and behavior that could potentially be improved

%prep
%setup -q -n %{archive_name}-%{version}
rm -rf *.egg-info

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

%build
%py2_build

%install
%py2_install

%check
# tests are still not working in EL6
# %{__python2} setup.py test

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{python2_sitelib}/%{lib_name}
%{python2_sitelib}/ansible_lint-%{version}-py2.*.egg-info

%changelog
* Mon Mar 20 2017 Parag Nemade <pnemade AT redhat DOT com> - 3.4.12-1
- Update to 3.4.12 version

* Fri Dec 05 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.0.1-1
- Update to 2.0.1

* Mon Oct 27 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.4-1
- rename to ansible-lint
- new upstream 1.0.4 release which added LICENSE file.

* Sat Oct 25 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-2
- Better add upstream LICENSE file, not present in tarball

* Wed Sep 24 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.0.2-1
- Initial packaging

