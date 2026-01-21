'use client';

import { useState } from 'react';
import Link from 'next/link';
import { 
  Cloud, 
  Award, 
  BookOpen, 
  CheckCircle, 
  Clock, 
  DollarSign, 
  Target,
  Zap,
  Users,
  TrendingUp,
  FileText,
  GraduationCap
} from 'lucide-react';

export default function AWSCertificationPage() {
  const [selectedCert, setSelectedCert] = useState<'practitioner' | 'architect'>('practitioner');

  const certifications = {
    practitioner: {
      name: 'AWS Cloud Practitioner',
      code: 'CLF-C02',
      level: 'Foundational',
      duration: '90 minutes',
      questions: 65,
      passingScore: '700/1000 (70%)',
      cost: '$100',
      studyTime: '2-4 weeks',
      color: 'from-blue-500 to-cyan-500',
      icon: Cloud,
      domains: [
        { name: 'Cloud Concepts', weight: '24%' },
        { name: 'Security & Compliance', weight: '30%' },
        { name: 'Cloud Technology & Services', weight: '34%' },
        { name: 'Billing, Pricing & Support', weight: '12%' }
      ],
      benefits: [
        'Perfect for AWS beginners',
        'Foundation for advanced certs',
        'Great resume starter',
        'Validates cloud fundamentals',
        'Opens cloud career paths'
      ],
      resources: [
        { title: 'Complete Guide', link: '/all/aws-cloud-practitioner', icon: BookOpen },
        { title: 'Quick Reference Cheatsheet', link: '/all/aws-quick-reference', icon: Zap },
        { title: 'Study Roadmap', link: '/all/aws-roadmap', icon: Target }
      ]
    },
    architect: {
      name: 'AWS Solutions Architect Associate',
      code: 'SAA-C03',
      level: 'Associate',
      duration: '130 minutes',
      questions: 65,
      passingScore: '720/1000 (72%)',
      cost: '$150',
      studyTime: '6-8 weeks',
      color: 'from-purple-500 to-pink-500',
      icon: Award,
      domains: [
        { name: 'Design Secure Architectures', weight: '30%' },
        { name: 'Design Resilient Architectures', weight: '26%' },
        { name: 'Design High-Performing Architectures', weight: '24%' },
        { name: 'Design Cost-Optimized Architectures', weight: '20%' }
      ],
      benefits: [
        'Industry-recognized credential',
        'Average 10-20% salary boost',
        'Opens architect/engineer roles',
        'Demonstrates practical skills',
        'Gateway to professional certs'
      ],
      resources: [
        { title: 'Complete Guide', link: '/all/aws-solutions-architect', icon: BookOpen },
        { title: 'Quick Reference Cheatsheet', link: '/all/aws-quick-reference', icon: Zap },
        { title: 'Study Roadmap', link: '/all/aws-roadmap', icon: Target }
      ]
    }
  };

  const cert = certifications[selectedCert];
  const Icon = cert.icon;

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900">
      {/* Header */}
      <div className="border-b border-white/10 bg-black/20 backdrop-blur-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center space-x-3">
            <Cloud className="w-8 h-8 text-cyan-400" />
            <h1 className="text-3xl font-bold text-white">AWS Certification Hub</h1>
          </div>
          <p className="mt-2 text-gray-300">Your complete guide to AWS certification success</p>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {/* Certification Selector */}
        <div className="flex flex-col sm:flex-row gap-4 mb-12">
          <button
            onClick={() => setSelectedCert('practitioner')}
            className={`flex-1 p-6 rounded-xl border-2 transition-all ${
              selectedCert === 'practitioner'
                ? 'border-cyan-400 bg-cyan-500/10 shadow-lg shadow-cyan-500/20'
                : 'border-white/10 bg-white/5 hover:border-white/20'
            }`}
          >
            <Cloud className={`w-12 h-12 mb-3 ${selectedCert === 'practitioner' ? 'text-cyan-400' : 'text-gray-400'}`} />
            <h3 className="text-xl font-bold text-white mb-1">Cloud Practitioner</h3>
            <p className="text-sm text-gray-400">Foundational • CLF-C02</p>
          </button>
          
          <button
            onClick={() => setSelectedCert('architect')}
            className={`flex-1 p-6 rounded-xl border-2 transition-all ${
              selectedCert === 'architect'
                ? 'border-purple-400 bg-purple-500/10 shadow-lg shadow-purple-500/20'
                : 'border-white/10 bg-white/5 hover:border-white/20'
            }`}
          >
            <Award className={`w-12 h-12 mb-3 ${selectedCert === 'architect' ? 'text-purple-400' : 'text-gray-400'}`} />
            <h3 className="text-xl font-bold text-white mb-1">Solutions Architect</h3>
            <p className="text-sm text-gray-400">Associate • SAA-C03</p>
          </button>
        </div>

        {/* Main Content */}
        <div className="grid lg:grid-cols-3 gap-8">
          {/* Left Column - Exam Details */}
          <div className="lg:col-span-2 space-y-6">
            {/* Exam Overview */}
            <div className={`bg-gradient-to-br ${cert.color} p-[2px] rounded-xl`}>
              <div className="bg-slate-900 rounded-xl p-8">
                <div className="flex items-center space-x-4 mb-6">
                  <Icon className="w-16 h-16 text-white" />
                  <div>
                    <h2 className="text-3xl font-bold text-white">{cert.name}</h2>
                    <p className="text-gray-300">{cert.code} • {cert.level}</p>
                  </div>
                </div>

                <div className="grid sm:grid-cols-2 md:grid-cols-4 gap-4">
                  <div className="bg-white/5 rounded-lg p-4">
                    <Clock className="w-6 h-6 text-cyan-400 mb-2" />
                    <p className="text-sm text-gray-400">Duration</p>
                    <p className="text-white font-semibold">{cert.duration}</p>
                  </div>
                  <div className="bg-white/5 rounded-lg p-4">
                    <FileText className="w-6 h-6 text-green-400 mb-2" />
                    <p className="text-sm text-gray-400">Questions</p>
                    <p className="text-white font-semibold">{cert.questions}</p>
                  </div>
                  <div className="bg-white/5 rounded-lg p-4">
                    <Target className="w-6 h-6 text-purple-400 mb-2" />
                    <p className="text-sm text-gray-400">Passing Score</p>
                    <p className="text-white font-semibold">{cert.passingScore}</p>
                  </div>
                  <div className="bg-white/5 rounded-lg p-4">
                    <DollarSign className="w-6 h-6 text-yellow-400 mb-2" />
                    <p className="text-sm text-gray-400">Cost</p>
                    <p className="text-white font-semibold">{cert.cost}</p>
                  </div>
                </div>
              </div>
            </div>

            {/* Exam Domains */}
            <div className="bg-white/5 backdrop-blur-sm rounded-xl p-6 border border-white/10">
              <h3 className="text-2xl font-bold text-white mb-4 flex items-center">
                <BookOpen className="w-6 h-6 mr-2 text-cyan-400" />
                Exam Domains
              </h3>
              <div className="space-y-3">
                {cert.domains.map((domain, idx) => (
                  <div key={idx} className="bg-white/5 rounded-lg p-4">
                    <div className="flex justify-between items-center mb-2">
                      <span className="text-white font-semibold">{domain.name}</span>
                      <span className="text-cyan-400 font-bold">{domain.weight}</span>
                    </div>
                    <div className="w-full bg-white/10 rounded-full h-2">
                      <div 
                        className={`bg-gradient-to-r ${cert.color} h-2 rounded-full transition-all duration-500`}
                        style={{ width: domain.weight }}
                      />
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Benefits */}
            <div className="bg-white/5 backdrop-blur-sm rounded-xl p-6 border border-white/10">
              <h3 className="text-2xl font-bold text-white mb-4 flex items-center">
                <TrendingUp className="w-6 h-6 mr-2 text-green-400" />
                Why Get Certified?
              </h3>
              <ul className="space-y-3">
                {cert.benefits.map((benefit, idx) => (
                  <li key={idx} className="flex items-start">
                    <CheckCircle className="w-5 h-5 text-green-400 mr-3 mt-0.5 flex-shrink-0" />
                    <span className="text-gray-300">{benefit}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {/* Right Column - Resources */}
          <div className="space-y-6">
            {/* Study Time */}
            <div className="bg-gradient-to-br from-orange-500 to-red-500 p-[2px] rounded-xl">
              <div className="bg-slate-900 rounded-xl p-6">
                <GraduationCap className="w-12 h-12 text-orange-400 mb-3" />
                <h3 className="text-xl font-bold text-white mb-2">Study Time</h3>
                <p className="text-3xl font-bold text-orange-400 mb-2">{cert.studyTime}</p>
                <p className="text-sm text-gray-400">2-3 hours per day</p>
              </div>
            </div>

            {/* Study Resources */}
            <div className="bg-white/5 backdrop-blur-sm rounded-xl p-6 border border-white/10">
              <h3 className="text-xl font-bold text-white mb-4 flex items-center">
                <BookOpen className="w-6 h-6 mr-2 text-cyan-400" />
                Study Resources
              </h3>
              <div className="space-y-3">
                {cert.resources.map((resource, idx) => (
                  <Link
                    key={idx}
                    href={resource.link}
                    className="flex items-center p-4 bg-white/5 hover:bg-white/10 rounded-lg border border-white/10 hover:border-cyan-400/50 transition-all group"
                  >
                    <resource.icon className="w-5 h-5 text-cyan-400 mr-3" />
                    <span className="text-white group-hover:text-cyan-400 transition-colors">
                      {resource.title}
                    </span>
                  </Link>
                ))}
              </div>
            </div>

            {/* Quick Stats */}
            <div className="bg-white/5 backdrop-blur-sm rounded-xl p-6 border border-white/10">
              <h3 className="text-xl font-bold text-white mb-4 flex items-center">
                <Users className="w-6 h-6 mr-2 text-purple-400" />
                What's Included
              </h3>
              <ul className="space-y-3 text-sm">
                <li className="flex items-center text-gray-300">
                  <CheckCircle className="w-4 h-4 text-green-400 mr-2" />
                  Complete exam guide (1500+ lines)
                </li>
                <li className="flex items-center text-gray-300">
                  <CheckCircle className="w-4 h-4 text-green-400 mr-2" />
                  {selectedCert === 'practitioner' ? '40' : '30'}+ practice questions
                </li>
                <li className="flex items-center text-gray-300">
                  <CheckCircle className="w-4 h-4 text-green-400 mr-2" />
                  Architecture patterns
                </li>
                <li className="flex items-center text-gray-300">
                  <CheckCircle className="w-4 h-4 text-green-400 mr-2" />
                  Hands-on lab scenarios
                </li>
                <li className="flex items-center text-gray-300">
                  <CheckCircle className="w-4 h-4 text-green-400 mr-2" />
                  Quick reference cheatsheet
                </li>
                <li className="flex items-center text-gray-300">
                  <CheckCircle className="w-4 h-4 text-green-400 mr-2" />
                  Exam strategies & tips
                </li>
              </ul>
            </div>

            {/* Start Learning CTA */}
            <Link
              href="/all/aws-cert-index"
              className="block w-full bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600 text-white font-bold py-4 px-6 rounded-xl text-center transition-all shadow-lg hover:shadow-cyan-500/50"
            >
              Start Your Journey →
            </Link>
          </div>
        </div>

        {/* Learning Path */}
        <div className="mt-12 bg-white/5 backdrop-blur-sm rounded-xl p-8 border border-white/10">
          <h3 className="text-2xl font-bold text-white mb-6 flex items-center">
            <Target className="w-6 h-6 mr-2 text-cyan-400" />
            Recommended Learning Path
          </h3>
          <div className="grid md:grid-cols-4 gap-4">
            <div className="bg-white/5 rounded-lg p-6 border-l-4 border-cyan-400">
              <div className="text-cyan-400 font-bold mb-2">Step 1</div>
              <h4 className="text-white font-semibold mb-2">Read Complete Guide</h4>
              <p className="text-sm text-gray-400">
                Study all exam domains thoroughly
              </p>
            </div>
            <div className="bg-white/5 rounded-lg p-6 border-l-4 border-purple-400">
              <div className="text-purple-400 font-bold mb-2">Step 2</div>
              <h4 className="text-white font-semibold mb-2">Hands-On Practice</h4>
              <p className="text-sm text-gray-400">
                Build real architectures in AWS
              </p>
            </div>
            <div className="bg-white/5 rounded-lg p-6 border-l-4 border-green-400">
              <div className="text-green-400 font-bold mb-2">Step 3</div>
              <h4 className="text-white font-semibold mb-2">Practice Questions</h4>
              <p className="text-sm text-gray-400">
                Complete 300+ practice questions
              </p>
            </div>
            <div className="bg-white/5 rounded-lg p-6 border-l-4 border-orange-400">
              <div className="text-orange-400 font-bold mb-2">Step 4</div>
              <h4 className="text-white font-semibold mb-2">Pass Exam!</h4>
              <p className="text-sm text-gray-400">
                Schedule and ace your certification
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
