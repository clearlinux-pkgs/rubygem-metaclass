#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-metaclass
Version  : 0.0.4
Release  : 5
URL      : https://rubygems.org/downloads/metaclass-0.0.4.gem
Source0  : https://rubygems.org/downloads/metaclass-0.0.4.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rubygems-tasks
BuildRequires : rubygem-test-unit

%description
Adds a `__metaclass__` method to all Ruby objects.
## Motivations
* Even though WhyTheLuckyStiff's [metaid gem](https://rubygems.org/gems/metaid) does something similar, apparently the metaclass method without underscores [doesn't play well with Rails v2.3](https://github.com/floehopper/mocha/commit/f0749d6d291164cc9280aa8ba16f33d652d45fe1#commitcomment-475799).
* I'm trying to extract code out of the [mocha gem](https://github.com/floehopper/mocha) and this is an obvious candidate.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n metaclass-0.0.4
gem spec %{SOURCE0} -l --ruby > rubygem-metaclass.gemspec

%build
gem build rubygem-metaclass.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
metaclass-0.0.4.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/metaclass-0.0.4 && sed -i '/require "bundler\/setup"/ d' test/test_helper.rb && ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)' && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/metaclass-0.0.4.gem
/usr/lib64/ruby/gems/2.2.0/doc/metaclass-0.0.4/ri/Metaclass/ObjectMethods/__metaclass__-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/metaclass-0.0.4/ri/Metaclass/ObjectMethods/cdesc-ObjectMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/metaclass-0.0.4/ri/Metaclass/cdesc-Metaclass.ri
/usr/lib64/ruby/gems/2.2.0/doc/metaclass-0.0.4/ri/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/metaclass-0.0.4/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/metaclass-0.0.4/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/metaclass-0.0.4/COPYING.txt
/usr/lib64/ruby/gems/2.2.0/gems/metaclass-0.0.4/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/metaclass-0.0.4/README.md
/usr/lib64/ruby/gems/2.2.0/gems/metaclass-0.0.4/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/metaclass-0.0.4/lib/metaclass.rb
/usr/lib64/ruby/gems/2.2.0/gems/metaclass-0.0.4/lib/metaclass/object_methods.rb
/usr/lib64/ruby/gems/2.2.0/gems/metaclass-0.0.4/lib/metaclass/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/metaclass-0.0.4/metaclass.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/metaclass-0.0.4/test/object_methods_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/metaclass-0.0.4/test/test_helper.rb
/usr/lib64/ruby/gems/2.2.0/specifications/metaclass-0.0.4.gemspec
